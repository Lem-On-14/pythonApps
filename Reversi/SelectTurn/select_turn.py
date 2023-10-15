# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.config import Config
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.properties import ObjectProperty

import sys
import numpy as np

#import reversi

Builder.load_file('./SelectTurn/select_turn.kv')

class SelectTurnWidget(FloatLayout):
    def makeWidget(self):
        return Factory.SelectTurnWidget()

    # def setStoneBlack(self):
    #     self.config.playerStone = 1
    #     self.config.computerStone = 2
    #     self.config.Turn = self.config.playerStone
    #     print("Black")  # 確認用
    # def setStoneWhite(self):
    #     self.config.playerStone = 2
    #     self.config.computerStone = 1
    #     self.config.Turn = self.config.computerStone
    #     print("White")  # 確認用
    pass

