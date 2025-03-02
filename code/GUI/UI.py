from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os

class Layout(BoxLayout):
    pass


class FirstApp(App):
    def build(self):
        return Layout()
    

if __name__ == "__main__":
    FirstApp().run()