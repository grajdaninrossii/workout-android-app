
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.metrics import dp

from Libs.uix.readart import ReadArt

# import io
# from kivy.core.image import Image as CoreImage

from Libs.programclass.WorkWithDB import WorkWithDB

Builder.load_file("./Libs/uix/kv/articles.kv")

#
class SelectedIconButton(MDIconButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_size)

    def set_size(self, interval):
        """
        Sets the custom icon size if the value of the `user_font_size`
        attribute is not zero. Otherwise, the icon size is set to `(48, 48)`.
        """

        self.width = (
            "48dp" if not self.user_font_size else self.user_font_size + dp(18)
        )
        self.height = (
            "48dp" if not self.user_font_size else self.user_font_size + dp(27)
        )

class SelectedBoxLayout(MDGridLayout):

    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)

        bd = WorkWithDB()

        self.number = id
        self.count = id

        # Присваиваем переменной публикации из БД
        art = bd.outPublication(id)
        # image = art[0][3]
        # Не работает с FitImage...
        # # load image from memory , as in  http://kivy.org/docs/api-kivy.core.image.html#in-memory-image-loading
        # data = io.BytesIO(image)
        # im = CoreImage(data, ext="jpg")
        # self.fImage.source = im.texture
        # Заполняем текст и картинку
        self.title_lable.text = art[0][1]
        self.article.text = '    ' + art[0][2]
        self.fImage.source = f"./Data/Images/{id}.jpg"
        self.card = ReadArt(id) # Создаем экран, для статьи

    def set_love(self):
        if self.like.icon != "heart":
            self.like.icon = "heart"
            self.like.text_color = 1, 0, 0, 1
            self.like.padding = (0, 0, 0, 0)
            self.like_stat.text = str(int(self.like_stat.text) + 1)
            # self.x += 1
            # print(self.x)
        else:
            self.like.icon = "heart-outline"
            self.like_stat.text = str(int(self.like_stat.text) - 1)
            self.like.text_color = 1, 1, 1, 0.9
            self.like.padding = (0, 0, 0, 0)

    pass

class Articles(ScrollView):
    view = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.upgrade_list)

    # Заполнение списка статей.
    def upgrade_list(self, list):
        self.list_widget = []
        for i in range(1, 8):
            self.list_widget.append(SelectedBoxLayout(i))
            self.artgrid.add_widget(self.list_widget[i-1])

class MyAppli(MDApp):

    def build(self):
        return Articles()

if __name__ == '__main__':
    MyAppli().run()
