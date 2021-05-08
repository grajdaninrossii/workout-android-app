from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

# from menu import SetToolbar # Не забыть убрать!!!!!1

#from kivy.core.window import Window # Убрать потом

#Window.size = (540, 860) # Убрать потом
from Libs.programclass.WorkWithDB import WorkWithDB

Builder.load_file("./Libs/uix/kv/registration.kv")


# Использование шрифта через LabelBase
# LabelBase.register(name = OpenSans,
#                    fn_regular = "IvyMode-Thin.ttf")

class Registration(Screen):
    # Авторизация
    def add_user(self):
        bd = WorkWithDB()

        if self.new_login.text != '' and self.new_password.text != '':
            if self.new_password.text == self.new_password_p.text:
# Формат добавления пользователя: массив(телефон, пароль, емаил, имя, гендер, дата рождения)
                data = [ self.phone.text,
                         self.new_password.text,
                         self.new_login.text,
                         '', # Имя
                         '', # Гендер
                         ''  # Пароль
                ]
            else:
                self.condition_enter.text_color = [1, 0, 0, 0.7]
                self.condition_enter.text = 'Вы не подтвердили пароль(Не одинаковые)!'
                return -1 # Ошибка ввода пароля
        else:
            self.condition_enter.text_color = [1, 0, 0, 0.7]
            self.condition_enter.text = 'Логин и пароль вводить обязательно!'
            return 1 # Ошибка ввода данных


        check = bd.addUser(data)
        if check != 0: # Ошибка добавления пользователя
            self.condition_enter.text_color = [1, 0, 0, 0.7]
            self.condition_enter.text = 'Такой пользователь уже зарегестрирован!'
        else: #Очистка
            self.new_login.text = ''
            self.new_password.text = ''
            self.new_password_p.text = ''
            self.phone.text = ''
            self.condition_enter.text_color = [0.12, 0.73, 0.50, 1]
            self.condition_enter.text = "Введите данные"
        return check


#
#
# class MainApp(MDApp):
#
#
#     def build(self):
#         self.title = "KivyMD Examples - Bottom Navigation11"
#         return Registration()
#
#
# if __name__ == "__main__":
#     MainApp().run()
