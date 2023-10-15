# -*- coding: utf-8 -*-
from kivy import app
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder

import FuncConst.funcConst as funcConst

import os
import sys
import numpy as np
import subprocess

#import reversi
#from reversi import Player, Computer, setField

Builder.load_file('./Menu/menu.kv')

class MenuWidget(BoxLayout):
    
    def makeWidget(self):

        try:

            return Factory.MenuWidget()

        except Exception as e:
            print(e)

class SelectMenuButtonAction(Button):

    def setExecPath(self, moveView):

        try:
            if moveView == "HelloWorld":
                funcConst.execPath = './UserMakeSrc/helloWorld.py'
                funcConst.questionPath = './Resources/Question/helloWorld.txt'
            if moveView == "TimesTables":
                funcConst.execPath = './UserMakeSrc/timesTables.py'
                funcConst.questionPath = './Resources/Question/timesTables.txt'

            self.root.gotoMakeCode()
                
        except Exception as e:
            print(e)
