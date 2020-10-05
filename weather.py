from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver

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

def overseas(where):
    url = "https://www.google.com/search?q=" + parse.quote(where + "+날씨")
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    bsObject = BeautifulSoup(html, "html.parser")
    bsObject = str(bsObject)

    print(bsObject)

    weather = bsObject.split ("<span class=\"vk_gy vk_sh\" id=\"wob_dc\">")[1].split ("<")[0]
    temp = bsObject.split ("<span class=\"wob_t\" id=\"wob_tm\" style=\"display:inline\">")[1].split ("<")[0]
    rainp = bsObject.split ("<span id=\"wob_pp\">")[1].split ("<")[0]
    humid = bsObject.split ("<span id=\"wob_hm\">")[1].split ("<")[0]
    wind = bsObject.split ("<span class=\"wob_t\" id=\"wob_ws\">")[1].split ("<")[0]
    htemp = bsObject.split ("<span class=\"wob_t\" style=\"display:inline\">")[1].split ("<")[0]
    ltemp = bsObject.split ("<span class=\"wob_t\" style=\"display:inline\">")[2].split ("<")[0]
    text1 = where + "의 기상정보\n\n" + "날씨: " + weather  + "\n" + "최저/최고 기온: " + ltemp + "º / " + htemp + "º\n" + "현재 기온: " + temp + "º\n" + "습도: " + humid + "\n" + "풍속: " + wind + "\n" + "강수확률: " + rainp

    return text1

if __name__ == '__main__':
    print(overseas("상해"))
