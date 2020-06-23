from enum import Enum

class Fic:


    def __init__(self, url : str):
        self.url = url
        self.title = ''
        self.author = ''
        self.file_name = ''
        self.website = Website.other

    def download_mobi(self):
        pass

    def get_data(self):
        pass

    def scrape_title(self):
        pass

class Website(Enum):
    ao3 = 1
    ffn = 2
    sb = 3
    sv = 4
    other = 5