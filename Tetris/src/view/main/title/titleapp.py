import kivy
kivy.require('1.11.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory

from kivy.lang import Builder
Builder.load_file('./play/tenplusapp.kv')
from play.tenplusapp import PlayWidget

class TitleWidget(FloatLayout):
    def gotoPlayDisplay(self):
        self.clear_widgets()
        self.add_widget(Factory.PlayWidget())
    pass

class TitleApp(FloatLayout):
    pass
