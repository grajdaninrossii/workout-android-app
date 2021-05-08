from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('kivy','window_icon','logo-workout.png')

from Libs.uix.menu import Menu
from Libs.uix.login import Login
from Libs.uix.registration import Registration
from Libs.uix.articles import Articles
from Libs.uix.readart import ReadArt
from Libs.uix.account import Account
from Libs.uix.training import Training
import sys

#from kivymd.uix.bottomnavigation import MDBottomNavigation

from kivy.core.window import Window # Убрать потом
# Window.size = (1080, 1920)
#Window.size = (540, 860) # Убрать потом

class MyApp(MDApp):

    number_art = 0 # Переменная для статей
    box = ObjectProperty()
    screen_manager = ScreenManager()
    screen_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard = self.onBackBtn)


    def onBackBtn(self, window, key, *args):
        # user presses back button
        if key == 27:
            # Check if there are any screens to go back to
            if self.screen_list:
                # if there are screens we can go back to, the just do it
                self.screen_manager.current = self.screen_list.pop()
                # Saw we don't want to close
                return True
            return False

    def changeScreen(self, next_screen):
        # operation = "addition subtaction multiplication division".split()
        # question = None

        if next_screen == "login":
            self.screen_manager.current = "login"

        # if screen is not alredy in the list fo prevous screens
        if self.screen_manager.current not in self.screen_list and self.screen_manager.current != "registration":
            self.screen_list.append(self.screen_manager.current)

        self.screen_manager.current = next_screen


    title = 'WORKOUT'

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        # Меняем цвет подстветки кнопок.
        self.theme_cls.primary_palette = ('Gray')

        # Пытаемся поменять икону...
        self.icon = "logo-workout.png"
        self.image = "first_screen.jpg"

        # Добавляем элементы в ScreenManager
        self.screen_manager.add_widget(Menu())

        self.screen_manager.add_widget(Registration())
        self.screen_manager.add_widget(Login())
        #self.screen_manager.add_widget(ReadArt())
        self.screen_manager.add_widget(Account())


        self.changeScreen("login")
        #self.screen_manager.current = "login"

        return self.screen_manager

    #
    def set_account(self):
        self.screen_manager.current = "account"


if __name__ == '__main__':
    MyApp().run()
