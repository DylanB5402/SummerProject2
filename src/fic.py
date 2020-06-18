from enum import Enum

class Fic:


    def __init__(self, url : str):
        self.url = url
        self.title = ''
        self.author = ''
        # if "archive" in url:
        #     self.website = Website.ao3
        # elif "fanfiction" in url:
        #     self.website = Website.ffn
        # elif "space" in url:
        #     self.website = Website.sb
        # elif "sufficient" in url:
        #     self.website = Website.sv
        # else:
        self.website = Website.other

    def get_mobi(self):
        pass

    def get_data(self):
        pass

class Website(Enum):
    ao3 = 1
    ffn = 2
    sb = 3
    sv = 4
    other = 5