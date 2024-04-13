import json

from openai import OpenAI

open_ai_token = "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"
client = OpenAI(
    api_key=open_ai_token,
)


def generate_response(messages):
    completion = client.chat.completions.create(  # Change the method name
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
    )
    return completion.choices[0].message.content


def add_message_chat_gpt(message, role):
    result = {
        "role": role,
        "content": message
    }
    return result


def get_prompt_message(id):
    file = open("backend/chat/prompt/prompts.json", "r", encoding="utf-8")
    data = json.load(file)
    prompts_message = data['prompt'][id]
    return prompts_message
