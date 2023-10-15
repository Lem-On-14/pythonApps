# -*- coding: utf-8 -*-
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

Builder.load_file('./ResultPage/resultHelloWorld.kv')

resourcesPath = './Resources/Alphabet/{}.png'

class MakeResultHelloWorldPageWidget(BoxLayout):

    def makeWidget(self):
        
        try:
            #画面生成
            resultWidget = Factory.MakeResultHelloWorldPageWidget()

            #helloworld.pyの実行
            ret = subprocess.run('python ' + funcConst.execPath, capture_output=True, text=True)

            #期待結果
            answer = 'HELLO WORLD'

            #実行結果の確認
            if ret.returncode == 0:
                #期待結果通りの場合
                if ret.stdout.rstrip() == answer:
                    strlist = list(ret.stdout)
                    for str in strlist:
                        filePath = resourcesPath.format(str)
                        #画面に結果を反映
                        if os.path.isfile(filePath):
                            img = Image(source=filePath)
                            resultWidget.ids.Result.add_widget(img)
                #期待結果通りでない場合
                else:
                    message = 'NOT COLECT\nYOUR ANSWER\n{}\nCOLECT ANSWER\n{}'
                    resultWidget.ids.Result.add_widget(Label(text=message.format(ret.stdout.rstrip(), answer), color=[1, 0, 0, 1]))
            #実行エラーの場合
            else:
                resultWidget.ids.Result.add_widget(Label(text='ERROR\n'+ret.stderr, color=[1, 0, 0, 1]))
            
            return resultWidget

        except Exception as e:
            print(e)
    