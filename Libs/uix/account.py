
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp


Builder.load_file("./Libs/uix/kv/account.kv")

class Account(Screen):
    pass


class MyApp(MDApp):

    def build(self):
        return Account()


if __name__ == '__main__':
    MyApp().run()
