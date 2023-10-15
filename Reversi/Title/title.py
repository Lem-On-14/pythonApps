# -*- coding: utf-8 -*-
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

Builder.load_file('./Title/title.kv')

class TitleWidget(FloatLayout):
    def makeWidget(self):
        return Factory.TitleWidget()

    pass
