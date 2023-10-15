from dataclasses import field
import kivy
kivy.require('1.11.1')

import numpy as np

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import ObjectProperty, NumericProperty
from kivy.factory import Factory

from kivy.core.window import Window
Window.size = (910, 720)

#from kivy.lang import Builder
#Builder.load_file('./title/titleapp.kv')

from common.gm import GM

class ColorWidget(Widget):
    def __init__(self, color, number, **kwargs):
        super(ColorWidget, self).__init__(**kwargs)
        self.color = color
        self.number = number
        self.size_hint = [None, None]
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()
    def update(self, *args):
        self.canvas.clear()
        self.canvas.add(Color(rgba=self.color))
        self.canvas.add(Rectangle(pos=self.pos, size=self.size))
        self.add_widget(Label(text=str(self.number), pos=self.pos, size=self.size))
    pass


class FieldWidget(Widget):
    nextMino = ObjectProperty(None)
    score = NumericProperty(0)
    field = None

    def __init__(self, **kwargs):
        super(FieldWidget, self).__init__(**kwargs)
        self.field = self.initField()
        self.wsize = 30         #self.width / 12
        self.hsize = 30         #self.height / 22
        self.size_hint = [None, None]
        self.size = [self.wsize * 12, self.hsize * 21]
        self.currentMino = GM.getRandomMino()
        self.currentMino.updateField(self.field)
        posList = list(zip(*np.where((self.field != 10) & (self.field != 0))))
        for pos in posList:
            self.field[(pos[0]+5,pos[1])] = self.field[pos]
            self.field[pos] = 0
        self.nextMino = None
        self.evt = None
        self.interval_time = 1
        self.blocksList = []
        self.cmList = []        # currentMinoList
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()

    def updateGrid(self, *args):
        self.canvas.add(Color(rgba=[0.85, 0.85, 0.85, 1]))
        for i in range(1, 22):
            self.canvas.add(Line(points=[self.x, self.y + self.hsize*i, self.x + self.wsize*12, self.y + self.hsize*i], width=1))
        for i in range(2, 11):
            self.canvas.add(Line(points=[self.x + self.wsize*i, self.y, self.x + self.wsize*i, self.y + self.hsize*21], width=1))
        pass

    def updateWalls(self, *args):
        posList = list(zip(*np.where(self.field == 10)))
        self.canvas.add(Color(rgba=[0, 0, 0, 1]))
        for pos in posList:
            # fieldの上部を表示させないためのIF文
            if(pos[0] > 4):
                self.canvas.add(Rectangle(pos=[self.x + int(self.wsize*pos[1]), self.y + int(self.hsize*(25-pos[0]))], size=[self.wsize, self.hsize]))
        pass

    def updateBlocks(self, *args):
          for cw in self.blocksList:
              # currentMino以外のミノを全て削除する
              self.remove_widget(cw)
          posList = list(zip(*np.where((0 < self.field) & (self.field < 10))))
          for pos in posList:
              if(pos[0] > 4):     # field上部を表示させないため
                  num = self.field[pos]
                  cw = ColorWidget(pos=[self.x + int(self.wsize*pos[1]), self.y + int(self.hsize*(25-pos[0]))],
                                   size=[self.wsize, self.hsize],
                                   color=[0.23, 0.08, 0.86, 0.5],
                                   number=num)
                  self.blocksList.append(cw)
                  self.add_widget(cw)
          pass

    def updateCurrentMino(self, *args):
        for cm in self.cmList:
            self.remove_widget(cm)
        if(self.currentMino != None):
            posList = list(zip(*np.where(self.currentMino.mino != 0)))
            for pos in posList:
                # fieldにおける座標を計算
                num = self.currentMino.mino[pos]
                ypos = self.currentMino.base[0] + pos[0]
                xpos = self.currentMino.base[1] + pos[1]
                if(ypos > 4):   # 上部を非表示にするため、動作確認時は、4を-1にする。
                    cw = ColorWidget(pos=[self.x + int(self.wsize*xpos), self.y + int(self.hsize*(25-ypos))],
                                     size=[self.wsize, self.hsize],
                                     color=[0.86, 0.08, 0.23, 0.5],
                                     number=num)
                    self.cmList.append(cw)
                    self.add_widget(cw)
        pass

    def update(self, *args):
        self.canvas.clear()
        self.canvas.add(Color(rgba=[1, 1, 1, 1]))
        self.canvas.add(Rectangle(pos=self.pos, size=self.size))
        self.updateGrid()
        self.updateWalls()
        self.clear_widgets()
        self.updateBlocks()
        self.updateCurrentMino()

    def rollLeft(self, *args):
        tof = self.currentMino.rollLeft(self.field)
        if(tof):
            self.updateCurrentMino()
    def rollRight(self, *args):
        tof = self.currentMino.rollRight(self.field)
        if(tof):
            self.updateCurrentMino()
    def moveLeft(self, *args):
        tof = self.currentMino.moveLeft(self.field)
        if(tof):
            self.updateCurrentMino()
    def moveRight(self, *args):
        tof = self.currentMino.moveRight(self.field)
        if(tof):
            self.updateCurrentMino()
    def moveUnder(self, *args):
        tof = self.currentMino.moveUnder(self.field)
        if(tof):
            self.updateCurrentMino()

    def initField(self):
        field = np.array([[10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 1
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 5
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 10
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 15
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 20
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10],
                  [10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10], # 25
                  [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]])

        # ランダムmino試し
        # mino = GM.getRandomMino()
        # mino.updateField(field)
        # posList = list(zip(*np.where((field != 10) & (field != 0))))
        # for pos in posList:
        #     field[(pos[0]+5,pos[1])] = field[pos]
        #     field[pos] = 0
        # print(field)
        return field

class PlayWidget(FloatLayout):
    def gotoTitleDisplay(self):
        self.clear_widgets()
        self.add_widget(Factory.TitleWidget())
    pass