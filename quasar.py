from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def init():
    global entire_list
    f = open("C:\\quasar.txt", 'r')
    entire_list = json.loads(f.read())
    f.close()

def implement():
    try:
        res = []
        url = "https://quasarzone.co.kr/bbs/qb_saleinfo"
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")

        span_items = bs.find_all('span')
        for span in span_items:
            span.extract()

        item = bs.find_all('a', attrs={'class': 'subject-link'})
        link = ["https://quasarzone.co.kr" + it.attrs['href'] for it in item]
        title = [it.text.replace('\"', "").replace('\'', '').strip() for it in item]

        for li, ti in zip(link[4:], title[4:]):
            if li in entire_list.keys():
                if ti == entire_list[li]:
                    continue
                res.append("제목 수정: " + entire_list[li] + " => " + ti + "\n" + li)
                entire_list[li] = ti
                save()
                continue
            entire_list[li] = ti
            save()
            res.append("신규 정보: " + ti + "\n" + li)
        return res
    except:
        pass

def save():
    f = open('C:\\quasar.txt', 'w')
    f.write(str(entire_list).replace("\"","").replace("\'", "\""))
    f.close()
