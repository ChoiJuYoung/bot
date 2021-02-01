from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from KakaoModule import Kakao

def get_info(name):
    bsObject = get_url(parse.quote(name))
    chk = bsObject.find('button', attrs={'id': 'btn-sync'})
    
    if chk.text.strip() == '정보갱신':
        update_history(name)
        
        bsObject = get_url(parse.quote(name))
        chk = bsObject.find('button', attrs={'id': 'btn-sync'})

    return bsObject

def update_history(name):
    driver = webdriver.Chrome('D:/chromedriver.exe')
    driver.get('https://maple.gg/u/' + name)
    btn = driver.find_element_by_id('btn-sync')
    btn.click()
    driver.implicitly_wait(1)

def get_url(url):
    url = "https://maple.gg/u/" + url
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject

def get_cody(name):
    bs = get_info(name)
    cody = [c.text for c in bs.find_all('span', attrs={'class':'character-coord__item-name'})]
    img = [i['src'] for i in bs.find('div', attrs={'id':'user-profile'}).find_all('img')]
    args = {'hat': cody[0], 'hair': cody[1], 'face': cody[2], 'up': cody[3], 'down': cody[4], 'shoes': cody[5], 'weapon': cody[6], 'img': img[0], 'name': name, 'server': img[2]}
    return [44234, args]
    
def kakao_send(room, template, args):
    KakaoLink.send(room, {
                    "link_ver": "4.0",
                    "template_id": template,
                    "template_args": args
                }, "custom")

if __name__ == '__main__':
    f = open('D:\\key.txt', 'r')
    key = f.read()
    key = key.split('\n')
    KakaoLink = Kakao(key[0])
    KakaoLink.login(key[1], key[2])
    cody = get_cody('funscream')
    kakao_send('주영', cody[0], cody[1])