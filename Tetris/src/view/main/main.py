import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import ObjectProperty, NumericProperty
from kivy.factory import Factory

from kivy.core.window import Window
Window.size = (910, 720)

from kivy.lang import Builder
Builder.load_file('./title/titleapp.kv')
from title.titleapp import TitleApp

class MainRoot(FloatLayout):
    
    def __init__(self, **kwargs):
        super(MainRoot, self).__init__(**kwargs)
        self.clear_widgets()
        self.add_widget(Factory.TitleWidget())

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = '画面切り替えテスト'

if __name__ == "__main__":
    MainApp().run()