from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup

def get_history(name):
    url = "https://maple.gg/u/" + parse.quote(name)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    print(bsObject)

    cody = bsObject.find_all('span', attrs={'class':'character-coord__item-name'})
    for c in cody:
        print(c.text)


if __name__ == '__main__':
    get_history('FunScream')