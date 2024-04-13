import json

import requests
from chat.chat_gpt import get_prompt_message, add_message_chat_gpt, generate_response
from chat.models import CountMessages
from config.settings import USER

API = 'AQVNwYdqvYu1jUVPNwkbRumeUAk41gtQJGmbs3KS'
CATALOG = 'b1g9ah45e9nb97tch5sf'


def get_start_json():
    start_json = {
        "modelUri": f"gpt://{CATALOG}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
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
    return send_message_ai(start_json)


def send_message_ai(start_json):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API}"
    }
    response = requests.post(url, headers=headers, json=start_json)
    result = response.json()
    return result


def set_info_student(message, count):
    prompt_message = get_prompt_message(count)
    messages = [{
        "role": 'system',
        "content": prompt_message['prompt']
    }]
    messages.append(add_message_chat_gpt(message, 'user'))
    return generate_response(messages)


def create_room():
    CountMessages.objects.create().save()


def get_count_user():
    message = CountMessages.objects.all().last()
    return message.count

def count_add_message():
    message = CountMessages.objects.all().last()
    message.count += 1
    message.save()


def get_next_message(id):
    prompt = get_prompt_message(id)
    return prompt['start_message']


def get_len_prompts():
    file = open("backend/chat/prompt/prompts.json", "r", encoding="utf-8")
    data = json.load(file)
    prompts_message = data['prompt']
    return len(prompts_message)