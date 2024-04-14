import json

from openai import OpenAI

open_ai_token = "open_ai_token"
client = OpenAI(
    api_key=open_ai_token,
)


def generate_response(messages):
    completion = client.chat.completions.create(  # Change the method name
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        max_tokens=1000,
    )
    return completion.choices[0].message.content



def get_prompt_message(id):
    file = open("backend/chat/prompt/prompts.json", "r", encoding="utf-8")
    data = json.load(file)
    prompts_message = data['prompt'][id]
    return prompts_message


def get_prompt_path_message(id):
    file = open("backend/chat/prompt/path_prompts.json", "r", encoding="utf-8")
    data = json.load(file)
    prompts_message = data['prompt'][id]
    return prompts_message
