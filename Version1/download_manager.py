import requests as r
import colorama as c
import Downloader as d
import downloadLog
import os

folder = './'

downloads = [
]

def download():
    for down in downloads:
        (readerLink, anime, saison, episode) = down
        print("| Downloading : {} > {} > {}".format(anime, saison, episode))
        readerLink = d.download(readerLink)

        if(readerLink == ''):
            downloadLog.log('| Error to download : {} > {} > {}'.format(anime, saison, episode))
            continue

        stream = r.get(readerLink, stream=True)

        if not os.path.exists(folder + anime):
            os.mkdir(folder + anime)
        if not os.path.exists(folder + anime + "/" + saison):
            os.mkdir(folder + anime + "/" + saison)

        filePath = folder + anime + "/" + saison + "/" + episode + ".mp4"
        if(os.path.exists(filePath)):
            continue
        f = open(filePath, 'wb')
        try:
            f.write(stream.content)
        except:
            downloadLog.log('| ERROR during (writing error) download : {} > {} > {}'.format(anime, saison, episode))
            print(c.Back.RED + "| Download failed !" + c.Back.BLACK)