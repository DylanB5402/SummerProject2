import os
import smtplib
from email import encoders
from email.mime import multipart, base

import password
import fanficfare_downloader

def send_fic(url : str, email_address : str, password : str, kindle_email):
    port = 587
    fic_filename = fanficfare_downloader.download_mobi_and_get_file_name(url)
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


send_fic('https://archiveofourown.org/works/746517', password.my_email, password.password, password.kindle_email)


