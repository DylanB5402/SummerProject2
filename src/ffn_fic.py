from fic import Fic, Website
from bs4 import BeautifulSoup
import requests

class FfnFic(Fic):

    def __init__(self, url : str):
        self.url = url

