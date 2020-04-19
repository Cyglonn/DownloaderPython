

def log(text):
    f = open('downloadLog.txt', 'a')
    f.write('\n' + text)
    f.close()