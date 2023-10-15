# -*- coding: utf-8 -*-
from kivy import config
from Common.computer import Computer
from Common.player import Player
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.lang import Builder
from Config.config import ConfigValue

import sys
import numpy as np

#import reversi
#from reversi import Player, Computer, setField

Builder.load_file('./Play/play.kv')

configValue = ConfigValue()
player = Player(0, 0)
comp = Computer(0, 0)

class PlayWidget(BoxLayout):
    def makeWidget_SetStoneBlack(self):
        PlayWidget.setPlayConfig(1, 2, 1)
        return PlayWidget.makeWidget()
    def makeWidget_SetStoneWhite(self):
        PlayWidget.setPlayConfig(2, 1, 1)
        return PlayWidget.makeWidget()

    def makeWidget():
        pw = Factory.PlayWidget()
        pw.ids.clb.text = '2'
        pw.ids.clw.text = '2'
        pw.ids.BlackTurn.text = 'You' if(configValue.playerStone == 1) else 'Computer'
        pw.ids.WhiteTurn.text = 'You' if(configValue.playerStone == 2) else 'Computer'
        pw.ids.TurnLabel.text = 'Turn : ' + pw.ids.BlackTurn.text
        return pw

    def setPlayConfig(playerStone, computerStone, turn):
        global configValue
        global player
        global comp

        configValue.playerStone = playerStone
        configValue.computerStone = computerStone
        configValue.turn = turn
        player = Player(playerStone, computerStone)
        comp = Computer(computerStone, playerStone)

class FieldWidget(Widget):

    field = np.array([[0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,2,1,0,0,0],
                  [0,0,0,1,2,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0]])

    def drawField(self):
        self.canvas.clear()
        self.canvas.add(Color(rgb=[0.281, 0.363, 0.246]))
        self.canvas.add(Rectangle(pos=self.pos, size=self.size))
        self.canvas.add(Color(rgb=[0, 0, 0]))
        self.canvas.add(Line(rectangle=[self.x, self.y, self.width, self.height], width=5))
        self.drawRowLine()
        self.drawColLine()
        self.drawStone()
        pass
    def drawRowLine(self):
        for i in range(1, 8):
            row = (self.height / 8 * i) + self.y
            rowLine = Line(width=3)
            rowLine.points = [self.x, row, self.width + self.x, row]
            self.canvas.add(rowLine)
            pass
    def drawColLine(self):
        for i in range(1, 8):
            col = (self.width / 8 * i) + self.x
            colLine = Line(width=3)
            colLine.points = [col, self.y, col, self.height + self.y]
            self.canvas.add(colLine)
            pass
    def drawStone(self):
        poscalc = lambda z, wh: (wh / 16) + (wh / 8) * z
        rad = self.width / 8 * 0.4
        for i in range(8):
            ypos = (self.height - poscalc(i, self.height)) + self.y
            for j in range(8):
                xpos = poscalc(j, self.width) + self.x
                num = self.field[(i, j)]
                if(num == 0):
                    pass
                elif(num == 1):
                    self.canvas.add(Color(rgb=[0, 0, 0]))
                    self.canvas.add(Ellipse(pos=[xpos-rad, ypos-rad], size=[rad*2, rad*2]))
                elif(num == 2):
                    self.canvas.add(Color(rgb=[1, 1, 1]))
                    self.canvas.add(Ellipse(pos=[xpos-rad, ypos-rad], size=[rad*2, rad*2]))
                    pass
                else:
                    print("FieldWidget drawField Error")
                    sys.exit()
    def on_touch_down(self, touch):
        xpos = int((touch.x - self.x) / (self.width / 8))
        ypos = int(8 - (touch.y - self.y) / (self.height / 8))
        print('(xpos, ypos) = (%s, %s)' %(str(xpos), str(ypos)))
        print('(turn) = (%s)' %(str(configValue.turn)))
        if(configValue.turn == configValue.playerStone):
            mypos = (ypos, xpos)
            if(len(player.getPossibleLocation(self.field)) == 0):
                configValue.turn = configValue.computerStone
                self.parent.parent.ids.TurnLabel.text = 'Turn : Computer'
            else:
                if(player.confPos(mypos, self.field)):
                    player.updateField(mypos, self.field)
                    self.drawField()
                    configValue.turn = configValue.computerStone
                    self.parent.parent.ids.TurnLabel.text = 'Turn : Computer'
            pass
        elif(configValue.turn == configValue.computerStone):
            mypos = comp.electRandom(self.field)
            if(mypos != None):
                comp.updateField(mypos, self.field)
                self.drawField()
            configValue.turn = configValue.playerStone
            self.parent.parent.ids.TurnLabel.text = 'Turn : You'
        else:
            pass
        self.parent.parent.ids.clb.text = str(len(list(zip(*np.where(self.field == 1)))))
        self.parent.parent.ids.clw.text = str(len(list(zip(*np.where(self.field == 2)))))
        if(len(player.getPossibleLocation(self.field)) == 0 and len(comp.getPossibleLocation(self.field)) == 0):
            self.parent.parent.ids.TurnLabel.text = self.confResult()

    def confResult(self):
        ps = len(list(zip(*np.where(self.field == configValue.playerStone))))
        cs = len(list(zip(*np.where(self.field == configValue.computerStone))))
        if(ps > cs):
            return 'Winner : You'
        elif(ps < cs):
            return 'Winner : Computer'
        else:
            return 'Result : Draw'

    pass