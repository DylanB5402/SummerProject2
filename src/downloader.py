from bs4 import BeautifulSoup
from fic import Fic
from ao3_fic import AO3Fic

def send_fic(url : str, send_email : str, password : str):
    if "archive" in url:
        fic = AO3Fic(url)
    # elif "fanfiction" in url:
    # elif "space" in url:
    # elif "sufficient" in url:
    else:
        fic = Fic(url)



