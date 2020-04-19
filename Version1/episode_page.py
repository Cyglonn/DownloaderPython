from bs4 import BeautifulSoup as bs
import requests as r

knownUploaders = ['rapidvideo']

def get_reader_link(url):
    vl = r.get(url)

    sp = bs(vl.text, 'html.parser')

    episodeId = sp.find('option', attrs={'selected': 'selected'}).get('episodeid')
    uploaders = sp.find('select', attrs={'id':'sel1'}).find_all_next('option')
    uploaders = [k.get('value') for k in uploaders if not k.get('value').isnumeric()]



    uploaders_dispo = list(set(uploaders) & set(knownUploaders))


    if(len(uploaders_dispo) == 0):
        return (True, "ERROR : pas d'uploader dispo")

    link = r.get('https://animesvostfr.net/ajax-get-link-stream/?server={}&filmId={}'.format(uploaders_dispo[0], episodeId)).text

    if link[:-1] == ' ':
        link = link[:-1]

    return (False, link)
