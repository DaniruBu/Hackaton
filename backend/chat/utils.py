import requests

from config.settings import USER

API = 'AQVNwYdqvYu1jUVPNwkbRumeUAk41gtQJGmbs3KS'
CATALOG = 'b1g9ah45e9nb97tch5sf'


def get_start_json():
    start_json = {
        "modelUri": f"gpt://{CATALOG}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 1500,
        },
        "messages": []
    }
    return start_json


def add_message(question, start_json, role):
    start_json['messages'].append({
        'role': role,
        'text': question,
    })
    return start_json


def get_answer_ai(question):
    start_json = get_start_json()
    start_json = add_message(question, start_json, USER)
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API}"
    }
    response = requests.post(url, headers=headers, json=start_json)
    result = response.json()
    return result
