import youtubedownloader as d
import requests as req
import os


url="https://youtubedownloader.cx/v/mzokx4er19q"
##url = input("url : ")
link = d.download(url)

stream = req.get(link, stream=True)
print(stream.url)
stream.close()
