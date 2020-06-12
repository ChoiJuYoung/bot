import json
import ssl
import os
from random import random

from flask import Flask, request, jsonify

import dialogflow_v2 as dialogflow
from google.cloud.bigquery.client import Client
from google.protobuf.json_format import MessageToJson

from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

from weather import getWeather
import memo as m

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath("/home/hajuu96/choco-bot-apikey.json")
# apikey 획득


def detect_intent_texts(text, id):
    session_client = dialogflow.SessionsClient()
    project_id = "choco-bot-dfyxjw"
    session_id = id
    language_code = "ko"
    session = session_client.session_path(project_id, session_id)
    
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    
    res = response.query_result.fulfillment_text
    
    return res

    
def returnForm(res):
    return "<!DOCTYPE HTML><html> \
    <head> \
        <title>ChocoBot</title> \
    </head> \
    <body> \
        <start> \
            " + str(res) + " \
        </start> \
    </body> \
    </html>"


app = Flask(__name__)

@app.route('/')
def reply():
    platform = request.args.get("platform")
    if platform == "link":
        return returnForm("None")


    #ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    #if not (ip.startswith('192.168.0.') or ip.startswith('127.0.0.')):
    #    return "ERR"
    room = request.args.get('room')
    msg = request.args.get('msg')
    sender = request.args.get('sender')
    isGroupChat = request.args.get('isGroupChat')
    
    if msg.startswith("!주사위"):
        value = int(random() * 101)
        return returnForm(str(value))
    elif msg.startswith("!동전"):
        value = int(random() * 398402) % 2
        if value == 0:
            return returnForm("앞면")
        else:
            return returnForm("뒷면")
    elif msg.startswith("!방무"):
        try:
            msg = msg.replace("!방무 ", "")
            lst = msg.split(" ")
            ret = 1.0
            for x in lst:
                ret *= (1 - 1.0 * int(x) / 100.0)
            ret = 1.0 - ret
            return returnForm("입력하신 방무의 총 방무는 " + str(int(ret * 100)) + "% 입니다.")
        except:
            return returnFrom("입력값이 잘못되었습니다. 입력 형식은<br>!방무 방무값1 방무값2 방무값3...입니다.")
    elif msg.replace(" ", "").startswith("!메모확인"):
        return returnForm(m.show_memo(sender))
    elif msg.replace(" ", "").startswith("!메모삭제"):
        try:
            msg = int(msg.replace(" ", "")[5:])
            m.del_memo(sender, int(msg))
            return returnForm("메모를 삭제했습니다.")
        except:
            return returnForm("잘못된 입력입니다.")
    elif msg.startswith("!메모 "):
        try:
            msg = msg[4:]
            m.set_memo(sender, msg)
            return returnForm("메모를 완료했습니다.")
        except:
            return returnForm("잘못된 입력입니다.")

    res = detect_intent_texts(msg, sender)
    if res == "fallback":
        res = "None"
    elif res.startswith("날씨:"):
        ress = getWeather(res[3:])
        res = ress[0].replace("\n", "<br>") + "MESSAGESPLIT" + ress[1].replace("\n", "<br>")
    elif res.startswith("메뉴:"):
        return returnForm("None")
        
    return returnForm(res)
    
m.init()
if __name__ == '__main__':
    app.run(host = '0.0.0.0')