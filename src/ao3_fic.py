from fic import Fic, Website

from lxml import html
from bs4 import BeautifulSoup
import requests

class AO3Fic(Fic):

    def __init__(self, url : str):
        self.url = url
        self.website = Website.ao3

    def download(self):
        pass

fanfic = AO3Fic('https://archiveofourown.org/works/746517')
# webpage = html.fromstring(requests.get(fanfic.url).content)
webpage = BeautifulSoup(requests.get(fanfic.url).content, "lxml")
# print(webpage.find_all("ul", class_ = "download").find("ul", class_ = "expandable secondary"))
# links = webpage.xpath('//a/@href')
print(webpage.find("li", class_ = "download"))
# print('--------------------')
# print(webpage.find_all("li", class_ = "download"))
#