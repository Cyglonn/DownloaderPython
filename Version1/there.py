import requests as r
import json


def download(url):
    res = r.post('https://there.to/api/source/' + url.split('/v/')[1])
    decoder = json.JSONDecoder()
    resObj = decoder.decode(res.text)

    return resObj["data"][1]["file"]