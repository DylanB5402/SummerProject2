from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.uix.label import Label

import os
import certifi

import downloader
import password

desired_font_size = 30


class DownloadScreen(BoxLayout):

    def __init__(self):
        super().__init__(orientation = 'vertical')
        super.add_widget(TextBox())
        # super.add_widget(Button(text = 'Send'))


class TextBox(TextInput):

    def __init__(self, text_hint : str):
        super().__init__()
        self.multiline = False
        self.size_hint = 1, 0.2
        self.hint_text = text_hint
        self.font_size = desired_font_size


class URLTextbox(TextBox):

    def __init__(self):
        super().__init__("Fanfic URL")


class DestinationEmailTextbox(TextBox):

    def __init__(self):
        super().__init__("Destination Email")


class SendButton(Button):

    def __init__(self):
        super().__init__()
        self.text = 'Send'
        self.size_hint = (0.7, 1)
        self.font_size = desired_font_size

    def on_press(self):
        fanfic_url = App.get_running_app().url_box.text
        App.get_running_app().progress_label.text = 'URL Received!'
        downloader.send_fic(fanfic_url, password.my_email, password.password, password.kindle_email)
        App.get_running_app().progress_label.text = 'Fanfic Sent!'


class ResetButton(Button):

    def __init__(self):
        super().__init__()
        self.text = 'Reset'
        self.size_hint = (0.3, 1)
        self.font_size = desired_font_size

    def on_press(self):
        App.get_running_app().url_box.text = ''
        App.get_running_app().progress_label.text = ''


class ProgressLabel(Label):

    def __init__(self):
        super().__init__()
        self.text = ''
        self.font_size = desired_font_size


class DownloadApp(App):

    url_box = URLTextbox()
    button = SendButton()
    reset_button = ResetButton()
    progress_label = ProgressLabel()

    def build(self):
        os.environ['SSL_CERT_FILE'] = certifi.where()
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.url_box)
        inner_layout = BoxLayout(orientation = 'horizontal')
        inner_layout.size_hint = (1, 0.3)
        inner_layout.add_widget(self.button)
        inner_layout.add_widget(self.reset_button)
        layout.add_widget(inner_layout)
        layout.add_widget(self.progress_label)
        return layout




DownloadApp().run()
