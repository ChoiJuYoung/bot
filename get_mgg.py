from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver


def get_history(name):
    url = "https://maple.gg/u/" + parse.quote(name)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    print(bsObject)

    chk = bsObject.find('button', attrs={'id': 'btn-sync'})
    if chk.text == '정보갱신':
        update_history(name)

    cody = bsObject.find_all('span', attrs={'class':'character-coord__item-name'})
    for c in cody:
        print(c.text)

def update_history(name):
    driver = webdriver.Chrome('D:/chromedriver.exe')
    driver.get('https://maple.gg/u/' + name)
    btn = driver.find_element_by_id('btn-sync')
    btn.click()


if __name__ == '__main__':
    get_history('FunScream')
    