from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DownloadScreen(BoxLayout):

    def __init__(self):
        super().__init__(orientation = 'vertical')
        super.add_widget(URLBox())
        # super.add_widget(Button(text = 'Send'))


class URLBox(TextInput):

    def __init__(self):
        super().__init__()
        self.multiline = False
        self.size_hint = 1, 0.2


class DownloadApp(App):

    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(URLBox())
        layout.add_widget(Button(text = 'Send', size_hint = (1, 0.3)))
        return layout

DownloadApp().run()
