from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup

'''
def getWeather(where):
    url = "https://search.naver.com/search.naver?query=" + parse.quote(where + "+날씨")
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    bsObject = str(bsObject)
    
    loc = bsObject.split("<em>")[7].split("<")[0]
    weather = bsObject.split("<p class=\"cast_txt\">")[1].split("아")[0]
    temp = bsObject.split("<span class=\"todaytemp\">")[1].split("<")[0]
    ltemp = bsObject.split("<span class=\"num\">")[1].split("<")[0]
    htemp = bsObject.split("<span class=\"num\">")[2].split("<")[0]
    ftemp = bsObject.split("<span class=\"num\">")[3].split("<")[0]
    mrain = bsObject.split("<span class=\"num\">")[8].split("<")[0]
    arain = bsObject.split("<span class=\"num\">")[9].split("<")[0]
    dust = bsObject.split("<span class=\"num\">")[5].split("<")[0]
    fdust = bsObject.split("<span class=\"num\">")[6].split("<")[0]
    ozone = bsObject.split("<span class=\"num\">")[7].split("<")[0]
    wind = bsObject.split("<span>")[47].split("<")[0]
    humid = bsObject.split("<span>")[63].split("<")[0]
    tmt = bsObject.split("<span class=\"todaytemp\">")[2].split("<")[0]
    tat = bsObject.split("<span class=\"todaytemp\">")[3].split("<")[0]
    tmw = bsObject.split("<p class=\"cast_txt\">")[2].split("<")[0]
    taw = bsObject.split("<p class=\"cast_txt\">")[3].split("<")[0]
    tmr = bsObject.split("<span class=\"num\">")[10].split("<")[0]
    tar = bsObject.split("<span class=\"num\">")[11].split("<")[0]
    datmt = bsObject.split("<span class=\"todaytemp\">")[4].split("<")[0]
    datat = bsObject.split("<span class=\"todaytemp\">")[5].split("<")[0]
    datmw = bsObject.split("<p class=\"cast_txt\">")[4].split("<")[0]
    dataw = bsObject.split("<p class=\"cast_txt\">")[5].split("<")[0]
    datmr = bsObject.split("<span class=\"num\">")[12].split("<")[0]
    datar = bsObject.split("<span class=\"num\">")[13].split("<")[0]
    t = bsObject.split("<span class=\"day_info\">")[2].split(" ")[0]
    dt = bsObject.split("<span class=\"day_info\">")[3].split(" ")[0]
    loc = loc.strip()
    text1 = (where + "의 기상 정보\n" + "(" + "위치: " + loc + ")" + "\n\n날씨: " + weather  + "음\n" + "최저/최고 기온: " + ltemp + "º / " + htemp + "º\n" + "현재 기온: " + temp + "º\n" + "체감온도: " + ftemp + "º\n" + "습도: " + humid + "%\n" + "풍속: " + wind + "m/s" + "\n오전 강수확률: " + mrain + "%" + "\n오후 강수확률: " + arain + "%" + "\n미세먼지: " + dust + "\n초미세먼지: " + fdust + "\n오존: " + ozone)
    text2 = ("내일(" + t + ") 날씨\n\n" + "오전: " + tmw + ", " + tmt + "º\n" + "강수확률: " + tmr + "%\n" + "오후: " + taw + ", " + tat + "º\n" + "강수확률: " + tar + "%\n\n\n" + "모레(" + dt + ") 날씨\n\n" + "오전: " + datmw + ", " + datmt + "º\n" + "강수확률: " + datmr + "%\n" + "오후: " + dataw + ", " + datat + "º\n" + "강수확률: " + datar + "%")
    
    return [text1, text2]
'''

def getWeather(where):
    url = "https://search.naver.com/search.naver?query=" + parse.quote(where + "+날씨")
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    loc = bsObject.find('div', attrs={'class':'weather_area'}).find('span', attrs={'class':'btn_select'}).text
    
    today = bsObject.find('div', attrs={'class': 'today_area'})
    temp = today.find('span', attrs = {'class': 'todaytemp'}).text + "˚"

    main = today.find('div', attrs={'class' : 'main_info'}).find('ul', attrs={'class': 'info_list'}).find_all('li')
    weather = main[0].text.split('아')[0]
    ltemp = main[1].text.split('/')[0].strip()
    htemp = main[1].text.split('/')[1].split(' ')[0]
    ftemp = main[1].text.split('체감온도 ')[1]

    sub = today.find('div', attrs={'class': 'sub_info'}).find_all('span', attrs={'class': 'num'})
    dust = sub[0].text
    fdust = sub[1].text
    ozone = sub[2].text

    wind = today.find('div', attrs={'class': 'info_list', 'class': 'wind'}).find('span').text
    humid = today.find('div', attrs={'class': 'info_list', 'class': 'humidity'}).find('span').text

    mr = bsObject.find_all('span', attrs={'class': 'point_time', 'class': 'morning'})
    ar = bsObject.find_all('span', attrs={'class': 'point_time', 'class': 'afternoon'})
    mrain = mr[0].find('span', attrs={'class': 'num'}).text
    arain = ar[0].find('span', attrs={'class': 'num'}).text
    tmr = mr[1].find('span', attrs={'class': 'num'}).text
    tar = ar[1].find('span', attrs={'class': 'num'}).text
    datmr = mr[2].find('span', attrs={'class': 'num'}).text
    datar = ar[2].find('span', attrs={'class': 'num'}).text

    tomo = bsObject.find('div', attrs={'class': 'tomorrow_area'}).find_all('div', attrs={'class': 'main_info', 'class':'morning_box'})
    tmt = tomo[0].find('span', attrs={'class': 'todaytemp'}).text
    tmw = tomo[0].find('p', attrs={'class': 'cast_txt'}).text
    tat = tomo[1].find('span', attrs={'class': 'todaytemp'}).text
    taw = tomo[1].find('p', attrs={'class': 'cast_txt'}).text

    da = bsObject.find('div', attrs={'class': 'day_after'}).find_all('div', attrs={'class': 'main_info', 'class':'morning_box'})
    datmt = da[0].find('span', attrs={'class': 'todaytemp'}).text
    datmw = da[0].find('p', attrs={'class': 'cast_txt'}).text
    datat = da[1].find('span', attrs={'class': 'todaytemp'}).text
    dataw = da[1].find('p', attrs={'class': 'cast_txt'}).text

    b = bsObject.find_all('li', attrs={'class':'date_info', 'class':'today'})
    t = b[1].find('span').text.split(" ")[0]
    dt = b[2].find('span').text.split(" ")[0]

    text1 = (where + "의 기상 정보\n" + "(" + "위치: " + loc + ")" + "\n\n날씨: " + weather  + "음\n" + "최저/최고 기온: " + ltemp + " / " + htemp + "\n" + "현재 기온: " + temp + "\n" + "체감온도: " + ftemp + "\n" + "습도: " + humid + "%\n" + "풍속: " + wind + "m/s" + "\n오전 강수확률: " + mrain + "%" + "\n오후 강수확률: " + arain + "%" + "\n미세먼지: " + dust + "\n초미세먼지: " + fdust + "\n오존: " + ozone)
    text2 = ("내일(" + t + ") 날씨\n\n" + "오전: " + tmw + ", " + tmt + "º\n" + "강수확률: " + tmr + "%\n" + "오후: " + taw + ", " + tat + "º\n" + "강수확률: " + tar + "%\n\n\n" + "모레(" + dt + ") 날씨\n\n" + "오전: " + datmw + ", " + datmt + "º\n" + "강수확률: " + datmr + "%\n" + "오후: " + dataw + ", " + datat + "º\n" + "강수확률: " + datar + "%")
    return [text1, text2]