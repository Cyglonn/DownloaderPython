import utils as u
import json as j
import search as s
import anime_page as a
import episode_page as e
import time as t
import download_manager as d

listeAnimes = []
forbiddenCarac = [ ':', '/', '\\']
u.clear()

cookie = {
    '__cfduid': 'dd86be56bec1453d0dcdb108830a1e4a11562062682'
}

def removeForb(text):
    res = text
    for carac in forbiddenCarac:
        res = res.replace(carac, '')
    return res

def mainMenu():
    global listeAnimes
    result = -1
    while result == -1:
        u.clear()
        print(str(len(listeAnimes)) + ' in list')
        print()
        result = u.menu(['Add', 'Download', 'Save download datas', 'Load download datas', 'Show dowload datas', 'Set cookie value', 'Quitter'], 'Choix : ')

    if(result == 0):
        back, episodes = searchAnime()
        if not back:
            listeAnimes += episodes
    elif(result == 1):
        d.downloads = listeAnimes
        d.download()
    elif(result == 2):
        f = open('./save.json', 'w')
        encoder = j.JSONEncoder()
        f.write(encoder.encode(listeAnimes))
        print('| Finish !')
    elif(result == 3):
        f = open('./save.json', 'r')
        listeAnimes = j.load(f)
    elif(result == 4):
        u.clear()
        for e in listeAnimes:
            print(e[1] + " > " + e[2] + " > " + e[3])
        print("")
        input()
    elif(result == 5):
        exit()


def searchAnime():
    result = s.search(input("anime : "), cookie)

    menu = ['Back']

    menu += [res[1] for res in result]

    choice = u.menu(menu, 'Anime choisi : ')

    if choice == 0:
        return (True, '')
    choice -= 1
    u.clear()

    anime = result[choice][1]
    print("| Getting informations about : " + anime)
    err, episodesPage = a.get_episodes_pages(result[choice][2], cookie)
    
    c = 1
    while(c == 1 or c == -1):
        u.clear()
        anime = removeForb(anime)
        c = u.menu(['Yes', 'No'], 'Does anime name is : {} ? : '.format(anime))
        if c != 0:
            anime = input('Anime name : ')


    c = 1
    saison = 'unknown'
    while(c == 1 or c == -1):
        saison = removeForb(saison)
        u.clear()
        c = u.menu(['Yes', 'No'], 'Does saison name is : {} ? : '.format(saison))
        if c != 0:
            saison = input('Saison name : ')



    print("| Getting informations about : " + anime)


    links = []

    for i in range(len(episodesPage)):
        err, link = e.get_reader_link(episodesPage[i], cookie)
        links.append((link, anime, saison, 'Episode ' + str(i)))

    u.clear()

    return (False, links)


while True:
    mainMenu()
