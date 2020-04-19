

from bs4 import BeautifulSoup as bs
import requests as r



def get_episodes_pages(url, cookie):
    
    vl = r.get(url, cookies=cookie)

    sp = bs(vl.text, 'html.parser')

    linksEl = sp.find_all('div', attrs={ 'class': 'les-title'})
    links = []

    for i in linksEl:
        links.append(i.find('a').get('href'))

    return (False, links)
