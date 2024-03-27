import re
import requests
from Response import *

base_url = "https://api.telegram.org/bot7172839256:AAFvz2LjdpEdj_MWrBnIws8QQtA6SLWAKKc"

def read_msg(offset):
    parameters = {
        "offset": offset
    }

    resp = requests.get(base_url + "/getUpdates", data=parameters)
    data = resp.json()

    # print(data)

    for result in data["result"]:
        send_msg(result)

    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def auto_answer(message):
    # Check if the message exists in the responses dictionary
    message = re.sub(r'[^a-zA-Z\s]', '', message).lower()
    message = re.sub(r'\s+', ' ', message).strip().lower()
    if message.lower() in responses:
        return responses[message]
    else:
        return "Sorry, I could not understand you! I am still learning and trying to get better at answering."

def send_msg(message):
    chat_id = message["message"]["chat"]["id"]
    text = message["message"]["text"]
    message_id = message["message"]["message_id"]
    answer = auto_answer(text)

    parameters = {
        "chat_id": chat_id,
        "text": answer,
        "reply_to_message_id": message_id
    }

    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)

offset = 0

while True:
    offset = read_msg(offset)
