from fic import Fic
from ao3_fic import AO3Fic
from email.mime import multipart, base
from email import encoders
import smtplib


def send_fic(url : str, email_address : str, password : str, kindle_email):
    port = 587
    if "archive" in url:
        fic = AO3Fic(url)
    # elif "fanfiction" in url:
    # elif "space" in url:
    # elif "sufficient" in url:
    else:
        fic = Fic(url)
    fic.download_mobi()
    email = smtplib.SMTP('smtp.gmail.com', port)
    email.ehlo()
    email.starttls()
    # password = input('Password:')
    email.login(email_address, password)

send_fic('https://archiveofourown.org/works/746517','dylanb5402@gmail.com','Shadow5402', 'dylanb5402@kindle.com')


