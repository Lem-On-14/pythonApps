# -*- coding: utf-8 -*-
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

import FuncConst.funcConst as funcConst
import subprocess

Builder.load_file('./ResultPage/resultTimesTable.kv')

resourcesPath = './Resources/Alphabet/{}.png'

class MakeResultTimesTablePageWidget(BoxLayout):

    def makeWidget(self):
        
        try:
            #画面生成
            resultWidget = Factory.MakeResultTimesTablePageWidget()

            #helloworld.pyの実行
            ret = subprocess.run('python ' + funcConst.execPath, capture_output=True, text=True)

            #期待結果
            answer = '01 02 03 04 05 06 07 08 09\n02 04 06 08 10 12 14 16 18\n03 06 09 12 15 18 21 24 27\n04 08 12 16 20 24 28 32 36\n05 10 15 20 25 30 35 40 45\n06 12 18 24 30 36 42 48 54\n07 14 21 28 35 42 49 56 63\n08 16 24 32 40 48 56 64 72\n09 18 27 36 45 54 63 72 81'

            #実行結果の確認
            if ret.returncode == 0:
                #期待結果通りの場合
                if ret.stdout.rstrip() == answer:
                    strlist = ret.stdout.rstrip().replace('\n', ' ').split(' ')

                    #1の段、2の段、等のように段ごとに表示
                    loopCnt = 1
                    for str in strlist:
                        #段の初めは格納するボックスレイアウトを初期化
                        if loopCnt % 9 == 1:
                            strGroupContent = BoxLayout(orientation="horizontal")

                        strGroupContent.add_widget(Label(text = str, color=[1, 0, 0, 1]))

                        #段の最後まで来たら画面に追加
                        if loopCnt % 9 == 0:
                            resultWidget.ids.Result.add_widget(strGroupContent)
                        
                        loopCnt += 1
                        
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
    