from flask import Flask, request, redirect
import os

import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput
from google.cloud.bigquery.client import Client
from google.protobuf.json_format import MessageToJson

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\choco-bot-apikey.json'

def detect_intent_texts(text, id):
    session_client = dialogflow.SessionsClient()
    project_id = "choco-bot-dfyxjw"
    session_id = id
    language_code = "ko"
    session = session_client.session_path(project_id, session_id)
    
    text_input = TextInput(text=text, language_code=language_code)

    query_input = QueryInput(text=text_input)

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
    platform  = request.args.get("platform")
    if platform == "green":
        return returnForm("None")

    room = request.args.get('room')
    msg = request.args.get('msg')
    sender = request.args.get('sender')
    isGroupChat = request.args.get('isGroupChat')

    res = detect_intent_texts(msg, sender)
    if res.startswith("메뉴:"):
        res = res[3:]
        ret = "TEMPLATE25325TEMPLATE" + res
        return returnForm(ret)

    return returnForm("None")

@app.route('/redirect/search')
def redirect_search():
    url = "https://search.naver.com/search.naver?query=" + request.args.get('query')
    return redirect(url)
    


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)

