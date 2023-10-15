from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SampleScreen(BoxLayout): #ユーザーインタフェースを初期化するクラス
    def __init__(self, **kwargs):
         super().__init__(**kwargs)

class SampleApp(App): #アプリケーションのロジックを記述するクラス
    def build(self):
        return SampleScreen()

SampleApp().run()