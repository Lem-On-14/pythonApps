# -*- coding: utf-8 -*-
from kivy import config
from Config.config import ConfigValue
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.lang import Builder

import sys
import numpy as np

#import reversi
#from reversi import Player, Computer, setField

from Title.title import TitleWidget
from SelectTurn.select_turn import SelectTurnWidget
from Play.play import PlayWidget

Builder.load_file('main.kv')

class RootWidget(FloatLayout):
    config = ConfigValue()

    def gotoTitle(self):
        self.clear_widgets()
        self.add_widget(TitleWidget.makeWidget(self))

    def gotoSelectTurn(self):
        self.clear_widgets()
        self.add_widget(SelectTurnWidget.makeWidget(self))

    def gotoPlayBlack(self):
        self.clear_widgets()
        self.add_widget(PlayWidget.makeWidget_SetStoneBlack(self))

    def gotoPlayWhite(self):
        self.clear_widgets()
        self.add_widget(PlayWidget.makeWidget_SetStoneWhite(self))

    pass

class ReversiApp(App):
    def build(self):
        root = RootWidget()
        root.gotoTitle()
        return root

if __name__ == '__main__':
    ReversiApp().run()