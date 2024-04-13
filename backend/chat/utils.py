
from .chat_gpt import get_prompt_message, generate_response
import json

from .chat_gpt import generate_response
from .models import MessageGPT



def set_info_student(message, count):
    prompt_message = get_prompt_message(count)
    messages = [{
        "role": 'system',
        "content": prompt_message['prompt']
    }]
    messages.append(add_message_chat_gpt(message, 'user'))
    return generate_response(messages)


def get_prompt_message():
    file = open("chat/prompt/prompts.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    result = data['prompt']
    return result


def add_message_chat_gpt(message, role):
    result = {
        "role": role,
        "content": message
    }
    return result


def check_prompt(message_user):
    answer = '1'
    if len(MessageGPT.objects.all()) == 0:
        prompt_message = "Если следующий текст это информация о пользователе и (или) его хобби ответь в таком стиле 1) хобби 2) хобби и так далее. Если написано не по этому шаблону верни 0"
        messages = []
        messages.append(add_message_chat_gpt(prompt_message, 'system'))
        messages.append(add_message_chat_gpt(message_user, 'user'))
        answer = generate_response(messages)
    if answer != '0':
        messages = []
        answer = get_prompt_message()
        all_messages = MessageGPT.objects.all()
        for message in all_messages:
            messages.append(add_message_chat_gpt(message.text, message.role))
            MessageGPT.objects.create(
                role=message.role,
                text=message.text
            ).save()
        messages.append(add_message_chat_gpt(answer, 'system'))
        messages.append(add_message_chat_gpt(message_user, 'user'))
        answer = generate_response(messages)
        MessageGPT.objects.create(
            role='assistant',
            text=answer
        )

        return answer
    else:
        return "Неверный ввод"
