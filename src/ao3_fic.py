from fic import Fic, Website
from bs4 import BeautifulSoup
import requests

class AO3Fic(Fic):

    def __init__(self, url : str):
        self.url = url
        self.website = Website.ao3
        self.download_url = ''
        self.title = ''
        self.webpage = BeautifulSoup(requests.get(self.url).content, "lxml")


    def download_mobi(self):
        self.scrape_title()
        self.scrape_download_url()
        r = requests.get(self.download_url, allow_redirects=True)
        self.file_name = self.title + '.mobi'
        open(self.file_name, 'wb').write(r.content)

    def scrape_title(self):
        header = self.webpage.find("h2", class_ = "title heading")
        self.title = header.contents[0].strip()

    def scrape_download_url(self):
        download_links = self.webpage.find("li", class_ = "download").find('ul', class_ = "expandable secondary")
        for x in download_links:
            x = str(x)
            if "mobi" in x:
                self.download_url = "https://archiveofourown.org" + x[x.index("/downloads") : x.index(">MOBI") - 1]

# fanfic = AO3Fic('https://archiveofourown.org/works/746517')
# fanfic = AO3Fic('https://archiveofourown.org/works/24781507')
# print(fanfic.download_url)
# fanfic.get_mobi()