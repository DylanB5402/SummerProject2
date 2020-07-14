import os
import smtplib
from email import encoders
from email.mime import multipart, base
from fanficfare import cli
import password


def send_fic(url : str, email_address : str, password : str, kindle_email):
    port = 587
    fic_filename = download_mobi_and_get_file_name(url)
    print('downloaded!')
    email = smtplib.SMTP('smtp.gmail.com', port)
    email.ehlo()
    email.starttls()
    # password = input('Password:')
    email.login(email_address, password)
    msg = multipart.MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = kindle_email
    msg['Subject'] = ''
    attachment = open(fic_filename, 'rb')
    p = base.MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % fic_filename)
    msg.attach(p)
    text = msg.as_string()
    email.sendmail(email_address, kindle_email, text)
    email.quit()
    attachment.close()
    os.remove(fic_filename)

def download_mobi_and_get_file_name(url : str):
    url = https_to_http(url)
    cli.main(argv= ["-f", "mobi", url])
    print("done!")
    files = os.listdir(os.curdir)
    for file in files:
        if file[-5:] == '.mobi':
            return file


def https_to_http(url : str):
    url = url[0:4] + url [5:]
    return url



