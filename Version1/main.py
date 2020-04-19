import search as s
import anime_page as a
import episode_page as e
import colorama as c

print(c.Fore.WHITE + c.Back.BLACK)
def clear():
    for i in range(100):
        print('')

clear()

result = s.search(input("anime : "))

clear()
for i in range(len(result)):
    header = c.Fore.WHITE + c.Back.BLACK
    headerA = c.Fore.WHITE + c.Back.BLACK
    if(i % 2 == 1):
        header = c.Fore.BLACK + c.Back.WHITE
    print('| ' + header + str(i) + ' - ' + result[i][1] + headerA)
choice = int(input("Anime a télécharger : "))
clear()
print("| Getting informations about : " + result[choice][1])
err, episodesPage = a.get_episodes_pages(result[choice][2])

links = []

for episodePage in episodesPage:
    err, link = e.get_reader_link(episodePage)
    links.append(link)

f = open('./result.txt', 'w')

text = ""
for line in links:
    text += line + '\n'

f.write(text)

print('| Finish ! Please watch result.txt.')

print(text)

import time as t
t.sleep(1)




clear()