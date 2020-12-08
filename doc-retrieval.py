import os.path
import urllib.request


def getDocument(url: str):
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    print(html)
    f = open("downloads/" + os.path.basename(url), 'w', encoding="utf8")
    f.write(html)
    f.close()

