import os

import requests

CATALOG = os.getenv('CATALOG')
API = os.getenv('API')


def get_answer_ai(question):
    start_json = {
        "modelUri": f"gpt://{CATALOG}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 1500,
        },
        "messages": [{
            'role': 'user',
            'text': question,
        }
        ]
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API}"
    }
    response = requests.post(url, headers=headers, json=start_json)
    result = response.json()
    return result
