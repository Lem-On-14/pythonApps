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

Builder.load_file('./MakeCode/makeCode.kv')

class MakeCodeWidget(BoxLayout):
    
    def makeWidget(self):

        try:
            codeWidget = Factory.MakeCodeWidget()

            # ファイル読み込み(問題文の読み込み)
            if os.path.isfile(funcConst.questionPath):
                text = MakeCodeWidget.loadFile(funcConst.questionPath)
                codeWidget.ids.LabelExplanatoryText.text = text
                print(text)

            # ファイル読み込み(作成済みのこーどがあるかの確認)
            if os.path.isfile(funcConst.execPath):
                text = MakeCodeWidget.loadFile(funcConst.execPath)
                codeWidget.ids.TextInputEditCode.text = text

            return codeWidget

        except Exception as e:
            print(e)
    
    def loadFile(path):
        try:
            text = ''
            # ファイル取得
            with open(path, encoding='utf-8', mode='r') as f:
                for line in f:
                    text = text + line
            return text

        finally:
           f.close()

class ButtonAction(Button):

    def confirmSaveFilePopup(self):
        try:
            content = BoxLayout(orientation="vertical")
            content.add_widget(Label(text="Save File?"))

            #ボタングループ
            buttonGroupContent = BoxLayout(orientation="horizontal")
            #OKボタン
            buttonOK = Button(text = 'OK')
            buttonGroupContent.add_widget(buttonOK)

            #キャンセルボタン
            buttonCancel = Button(text="Cancel")
            buttonGroupContent.add_widget(buttonCancel)

            #popup設定
            content.add_widget(buttonGroupContent)
            popup = Popup(title='Confirmation',
                content=content,
                size_hint=(None, None), size=(400, 400))

            #アクション設定
            #OKボタン
            buttonOK.bind(
                on_press = lambda button: self.saveFile(),
                on_release = popup.dismiss
            )

            #キャンセルボタン
            buttonCancel.bind(on_release=popup.dismiss)

            popup.open()
        except Exception as e:
            print(e)

    def savedPopup(self):
        try:
            content = BoxLayout(orientation="vertical")
            content.add_widget(Label(text="Complete"))

            #閉じるボタン
            buttonClose = Button(text="Close")
            content.add_widget(buttonClose)

            #popup設定
            popup = Popup(title='Confirmation',
                content=content,
                auto_dismiss=True,
                size_hint=(None, None), size=(400, 400))

            #閉じるボタン
            buttonClose.bind(on_release=popup.dismiss)
            
            popup.open()
        except Exception as e:
            print(e)

    def saveFile(self):

        try:
            code = self.parent.parent.parent.parent.ids.TextInputEditCode.text
            print(code)

            with open(funcConst.execPath, mode='w') as f:
                f.write(code)
            
            self.savedPopup()
    
        finally:
            f.close()
