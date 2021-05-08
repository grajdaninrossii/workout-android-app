
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp

from Libs.programclass.WorkWithDB import WorkWithDB


Builder.load_file("./Libs/uix/kv/readart.kv")


class ReadArt(Screen):

    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)

        # Поключаем базу данных
        bd = WorkWithDB()

        # Сохраняем новое имя
        self.name = f"Readart_{id}"
        # Присваиваем переменной публикации из БД
        art = bd.outPublication(id)

        # Заполняем скрин данными из БД
        self.title.text = art[0][1]
        self.txt.text = '    ' + art[0][2]
        self.img.source = f"Data/Images/{id}.jpg"

class MyAppli(MDApp):

    def build(self):
        return ReadArt()


if __name__ == '__main__':
    MyAppli().run()
