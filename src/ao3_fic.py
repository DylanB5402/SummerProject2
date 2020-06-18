from fic import Fic, Website

from lxml import html
import bs4
from bs4 import BeautifulSoup
import requests

class AO3Fic(Fic):

    def __init__(self, url : str):
        self.url = url
        self.website = Website.ao3
        self.download_url = ''

    def get_mobi(self):
        pass

    def get_download_url(self):
        webpage = BeautifulSoup(requests.get(self.url).content, "lxml")
        download_links = webpage.find("li", class_ = "download").find('ul', class_ = "expandable secondary")
        for x in download_links:
            x = str(x)
            if "mobi" in x:
                self.download_url = "https://archiveofourown.org" + x[x.index("/downloads") : x.index(">MOBI") - 1]

# fanfic = AO3Fic('https://archiveofourown.org/works/746517')
fanfic = AO3Fic('https://archiveofourown.org/works/24781507')
fanfic.get_download_url()

