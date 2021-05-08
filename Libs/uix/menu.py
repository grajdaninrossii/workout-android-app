from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import ScreenManager, Screen
import sys

Builder.load_file("./Libs/uix/kv/menu.kv")


# Использование шрифта через LabelBase
# LabelBase.register(name = OpenSans,
#                    fn_regular = "IvyMode-Thin.ttf")

# Общие настройки шапки
class SetToolbar(MDToolbar):

    # Меняем шрифт MDToolbar/
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font_name)
        Clock.schedule_once(self.set_toolbar_font_size)
        Clock.schedule_once(self.set_toolbar_text_color)

    # Меняем шрифт тулбара.
    def set_toolbar_font_name(self, *args):
        self.ids.label_title.font_name = "./Data/Fonts/MMD-Regular.ttf"

    # Меняем размер.
    def set_toolbar_font_size(self, *args):
        self.ids.label_title.font_size = '25sp'

    # Меняем цвет текста.
    def set_toolbar_text_color(self, *args):
        self.ids.label_title.text_color = (0.12, 0.73, 0.5, 1)


class Menu(Screen):
    pass


# class MainApp(MDApp):
#
#     def build(self):
#         self.title = "KivyMD Examples - Bottom Navigation"
#         return Menu()
#
#
# if __name__ == "__main__":
#     MainApp().run()
