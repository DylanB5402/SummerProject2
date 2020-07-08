from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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
        self.size_hint = (1, 0.3)
        self.font_size = desired_font_size

    def on_press(self):
        fanfic_url = App.get_running_app().url_box.text
        # destination_email = App.get_running_app().destination_box.text
        # print(fanfic_url, destination_email)
        downloader.send_fic(fanfic_url, password.my_email, password.password, password.kindle_email)


class DownloadApp(App):

    url_box = URLTextbox()
    button = SendButton()
    # destination_box = DestinationEmailTextbox()

    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.url_box)
        # layout.add_widget(self.destination_box)
        layout.add_widget(self.button)
        return layout


DownloadApp().run()
