from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
# from menu import SetToolbar



#from kivy.core.window import Window # Убрать потом

#Window.size = (540, 860) # Убрать потом

Builder.load_file("./Libs/uix/kv/login.kv")

from Libs.programclass.WorkWithDB import WorkWithDB

# Использование шрифта через LabelBase
# LabelBase.register(name = OpenSans,
#                    fn_regular = "IvyMode-Thin.ttf")

class Login(Screen):

    # Авторизация
    def check_user(self):
        bd = WorkWithDB()

        check = bd.autorization(self.login.text, self.password.text)
        # Очистка записанных данных
        self.login.text = ''
        self.password.text = ''
        if check == 0:
            self.condition.text_color = [0.12, 0.73, 0.50, 1]
            self.condition.text = "Введите данные"
        return check

    def error(self, auto):
        self.condition.text_color = [1, 0, 0, 0.7]
        if auto == 1:
            self.condition.text = "Неверный логин или пароль! Зарегистрируйтесь!"



class MainApp(MDApp):


    def build(self):
        self.title = "KivyMD Examples - Bottom Navigation"
        return Login()


if __name__ == "__main__":
    MainApp().run()
