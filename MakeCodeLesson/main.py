# -*- coding: utf-8 -*-
import subprocess
from kivy import config
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.core.window import Window

import japanize_kivy

import FuncConst.funcConst as funcConst

from Menu.menu import MenuWidget
from MakeCode.makeCode import MakeCodeWidget
from ResultPage.resultHelloWorld import MakeResultHelloWorldPageWidget
from ResultPage.resultTimesTable import MakeResultTimesTablePageWidget

Builder.load_file('main.kv')

Window.size = (1200, 700)

class RootWidget(FloatLayout):

    def gotoMenu(self):
        self.clear_widgets()
        self.add_widget(MenuWidget.makeWidget(self))

    def gotoMakeCode(self):
        self.clear_widgets()
        self.add_widget(MakeCodeWidget.makeWidget(self))

    def gotoResultMakeCode(self):
        self.clear_widgets()

        if(funcConst.execPath == "./UserMakeSrc/helloWorld.py"):
            self.add_widget(MakeResultHelloWorldPageWidget.makeWidget(self))
        elif(funcConst.execPath == "./UserMakeSrc/timesTables.py"):
            self.add_widget(MakeResultTimesTablePageWidget.makeWidget(self))

class ExecOtherFileApp(App):
    def build(self):
        root = RootWidget()
        root.gotoMenu()
        return root

if __name__ == '__main__':
    ExecOtherFileApp().run()