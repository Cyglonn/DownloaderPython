
from colorama import Back, Fore

def clear():
    print(Fore.WHITE + Back.BLACK)
    for i in range(100):
        print('')

def menu(items, question):
    for i in range(len(items)):
        header = Fore.WHITE + Back.BLACK
        headerA = Fore.WHITE + Back.BLACK
        if(i % 2 == 1):
            header = Fore.BLACK + Back.WHITE
        print(header + str(i) + ' - ' + items[i] + headerA)
    print('')
    res = -1
    try:
        res = int(input(question))
    except:
        return -1
    if res not in range(len(items)):
        return -1
    return res