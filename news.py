from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup

def getNews():
    try:
        url = "https://news.daum.net/"
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")

        link = []
        title = []
        for i in range(1, 5):
            hd = bsObject.find('li', attrs={'data-tiara-layer':'cluster' + str(i)}).find('div', attrs={'class':'cont_thumb'}).find('a')
            link.append(hd.attrs['href'])
            title.append(hd.text)
        
        res = "--- 전체 뉴스 ---\n"
        for i in range(0, 4):
            res += "Title: " + title[i] + "\n"
            res += "link: " + link[i] + "\n"
            res += "\n"

        ########################################
        url = "https://news.daum.net/digital#1"
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")

        link = []
        title = []
        for i in range(2, 6):
            hd = bsObject.find('li', attrs={'data-tiara-layer':'MCC cluster' + str(i)}).find('div', attrs={'class':'cont_thumb'}).find('a')
            link.append(hd.attrs['href'])
            title.append(hd.text)
            
        res += "--- IT 뉴스 ---\n"
        for i in range(0, 4):
            res += "Title: " + title[i] + "\n"
            res += "link: " + link[i] + "\n"
            res += "\n"

        return(res.strip())
    except:
        return("NEWS ERROR")

if __name__ == '__main__':
    print(getNews())