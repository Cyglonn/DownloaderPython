import requests as r
import colorama as c
import os

folder = './'

downloads = [
]

def download():
    for down in downloads:
        print("| Downloading : " + down)

        stream = r.get(down, stream=True)

        filePath = "file1.mp4"
        if(os.path.exists(filePath)):
            continue
        f = open(filePath, 'wb')
        try:
            f.write(stream.content)
        except:
            print(c.Back.RED + "| Download failed !" + c.Back.BLACK)