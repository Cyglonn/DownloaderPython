import urllib.parse as urlParser
from bs4 import BeautifulSoup as bs
import requests as r

def search(query, cookie):
    '''


    result : 

    list obj : (id, title, urlPage, urlThumbnail)
    '''
    res = urlParser.quote(query)
    vl = r.get("https://animesvostfr.net/?s=" + res, cookies=cookie)
    sp = bs(vl.text, 'html.parser')

    htmlElements = sp.find("div", attrs={ 'class', 'movies-list movies-list-full' }).find_all_next('div', attrs={'class', 'ml-item' })
    
    result = []

    for element in htmlElements:
        id = element.get('data-movie-id')
        link = element.find_next('a').get('href')
        title = element.find_next('a').get('oldtitle')
        urlThumbnail = element.find_next('a').find_next('img').get('src')

        result.append((id, title, link, urlThumbnail))

    return result 