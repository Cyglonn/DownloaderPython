import youtubedownloader
import there
import hydrax

platforms = [

    ('https://youtubedownloader.cx/', youtubedownloader.download),
    ('https://there.to/', there.download),
    ('https://hydrax.net/', hydrax.download)           ## Vf avec plus de skill ;)
]

def download(url):
    for s in platforms:
        id = s[0]
        if(id in url):
            return s[1](url)
    print('Unknown url.')

