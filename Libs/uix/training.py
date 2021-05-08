
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp

from Libs.uix.articles import SelectedIconButton


Builder.load_file("./Libs/uix/kv/training.kv")

class Training(Screen):
    pass


class MyApp(MDApp):

    def build(self):
        return Training()


if __name__ == '__main__':
    MyApp().run()
