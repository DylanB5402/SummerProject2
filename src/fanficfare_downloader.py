from fanficfare import cli
import os


def download_mobi_and_get_file_name(url : str):
    cli.main(argv= ["-f", "mobi", url])
    files = os.listdir(os.curdir)
    for file in files:
        if file[-5:] == '.mobi':
            return file

