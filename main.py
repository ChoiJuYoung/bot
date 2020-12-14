import win32gui, time
from datetime import datetime
from weather import getWeather
import quasar as q
from news import getNews

def sendMsg(room, msg):
    try:
        hwnd1 = win32gui.FindWindow(None, room)
        hwnd2 = win32gui.FindWindowEx(hwnd1, 0, "RICHEDIT50W", "")
        win32gui.SendMessage(hwnd2, 0x000c, 0, msg)
        win32gui.PostMessage(hwnd2, 0x0100, 0xD, 0x1C001)
        print("LOG: [" + room + "] :" + msg)
    except:
        print("ERR: [" + room + "] :" + msg)

def sendWeather(room, where):
    for x in getWeather(where):
        sendMsg(room, x)
        time.sleep(1)

def getTime():
    now = datetime.now()

    return get2(now.hour) + get2(now.minute)

def get2(text):
    tmp = str(text)
    if len(tmp) < 2:
        tmp = "0" + tmp

    return tmp

def Yujeong():
    if int(datetime.now().weekday()) >= 5:
        return False
    return True

def true():
    return True

def false():
    return False

msgList = []
q.init()
quasar = []
        
weather = [
    ["0700", "병신톡", "서울시 동대문구 회기동", true],
    ["0630", "병신톡", "서울시 영등포구 여의도동", Yujeong],
    ["0800", "3인팟", "서울시 송파구 가락동", true],
    ["0730", "3인팟", "서울시 도봉구 창5동", true],
    ["0830", "서산", "서산시 동문1동", true],
    ["0830", "서산", "용인시 수지구 죽전동", true]
]

weather_list = [False] * len(weather)

msgList.append([weather, weather_list, "날씨"])


alarm = [
    #["2055", "서산", "@임동훈 @이성표 @최주영 모여라", true],
    ["0830", "주영", "유산균 먹고가자", true]
    ,["2200", "주영", "비타민 먹자", true]
    ,["1900", "S급 뒤틀린 파풀마 먹는방", "우르스 하세요.", true]
    ,["2230", "S급 뒤틀린 파풀마 먹는방", "우르스 하셨나요?", true]
    ,["2245", "S급 뒤틀린 파풀마 먹는방", "일퀘 일보 우르스 유니온 하세요."]
    ,["2330", "S급 뒤틀린 파풀마 먹는방", "펀치킹 치셨나요? 으쯔라구요~ 치셨나요? 치셨어요? 으쯔라구요~ 치셨어요? 어쩌라구요~"]
]

alarm_list = [False] * len(alarm)
news_list = False

msgList.append([alarm, alarm_list, "MSG"])


while True:
    try:
        now = getTime()
    
        for lst in msgList:
            for i in range(len(lst[0])):
                if not lst[1][i] and lst[0][i][0] == now and lst[0][i][3]():
                    if lst[2] == "날씨":
                        sendWeather(lst[0][i][1], lst[0][i][2])
                    elif lst[2] == "MSG":
                        sendMsg(lst[0][i][1], lst[0][i][2])
                    lst[1][i] = True

        if now == "2359":
            for lst in msgList:
                lst[1] = [False] * len(lst[0])
            news_list = False

        quasar += q.implement()
        if(now == "0800" or now == "1400" or now == "2000"):
            qres = ""
            for qu in quasar:
                qres += (qu + "\n")

            if qres != "":
                sendMsg("병신톡", qres)
            quasar = []

        if now == "0630" and not news_list:
            sendMsg("병신톡", getNews())
            news_list = True

        time.sleep(20)
    except:
        continue