from fic import Fic
from ao3_fic import AO3Fic
from email.mime import multipart, base
from email import encoders
import smtplib
import password
import os


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
    msg = multipart.MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = kindle_email
    msg['Subject'] = ''
    attachment = open(fic.file_name, 'rb')
    p = base.MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % fic.file_name)
    msg.attach(p)
    text = msg.as_string()
    email.sendmail(email_address, kindle_email, text)
    email.quit()
    attachment.close()
    os.remove(fic.file_name)

send_fic('https://archiveofourown.org/works/746517', password.my_email, password.password, password.kindle_email)


