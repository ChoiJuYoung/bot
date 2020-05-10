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

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\choco-bot-apikey.json'
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
    room = request.args.get('room')
    msg = request.args.get('msg')
    sender = request.args.get('sender')
    isGroupChat = request.args.get('isGroupChat')
    
    if msg == "!주사위":
        value = int(random() * 101)
        return returnForm(str(value))
    elif msg == "!동전":
        value = int(random() * 398402) % 2
        if value == 0:
            return returnForm("앞면")
        else:
            return returnForm("뒷면")


    res = detect_intent_texts(msg, sender)
    if res == "fallback":
        res = "None"
    elif res.startswith("날씨:"):
        ress = getWeather(res[3:])
        res = ress[0].replace("\n", "<br>") + "MESSAGESPLIT" + ress[1].replace("\n", "<br>")
        
    return returnForm(res)
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0')