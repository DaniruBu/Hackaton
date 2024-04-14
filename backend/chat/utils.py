
from .chat_gpt import get_prompt_message, generate_response
import json

<<<<<<< HEAD
from chat.chat_gpt import generate_response
from chat.models import HobbyGPT
from chat.models import MessageGPT
>>>>>>> origin/topando/chat_gpt
=======
from .chat_gpt import generate_response
from .models import MessageGPT

>>>>>>> origin/Daryutin/frontChats


def set_info_student(message, count):
    prompt_message = get_prompt_message(count)
    messages = [{
        "role": 'system',
        "content": prompt_message['prompt']
    }]
    messages.append(add_message_chat_gpt(message, 'user'))
    return generate_response(messages)


<<<<<<< HEAD
def get_prompt_message(prompt_id):
    file = open("backend/chat/prompt/prompts.json", "r", encoding="utf-8")
=======
def get_prompt_message():
    file = open("chat/prompt/prompts.json", "r", encoding="utf-8")
>>>>>>> origin/Daryutin/frontChats
    data = json.load(file)
    file.close()
    result = data['prompt'][prompt_id]
    return result


def add_message_chat_gpt(message, role):
    result = {
        "role": role,
        "content": message
    }
    return result


def check_prompt(message_user, prompt_id):
    messages = []
    answer = get_prompt_message(prompt_id)
    all_messages = MessageGPT.objects.all()
    for message in all_messages:
        messages.append(add_message_chat_gpt(message.text, message.role))
    messages.append(add_message_chat_gpt(answer, 'system'))
    messages.append(add_message_chat_gpt(message_user, 'user'))
    answer = generate_response(messages)

    return answer


def get_hobby(answer):
    answer = eval(answer)
    if 'hobby' in answer.keys():
        for hobby in answer['hobby']:
            if HobbyGPT.objects.filter(name=hobby).first() is None:
                HobbyGPT.objects.create(name=hobby).save()
        return True
    else:
<<<<<<< HEAD
        return "Неверный ввод"
<<<<<<< HEAD
>>>>>>> origin/topando/chat_gpt
=======
        return False


def sorting_event():
    result_list = "Рекумендую тебе мероприятия\n"
    hobbies = HobbyGPT.objects.all()
    hobbies_name = []
    for hobby in hobbies:
        hobbies_name.append(hobby.name)
    groups = [
        ["Плавание", "Это круто", ["плавание", "футбол", "гребля"]],
        ["Футбол", "Это круто", ["плавание", "баскетбол", "футбол"]],
        ["баскетбол", "Это круто", ["баскетбол", "волейбол"]],
        ["Гребля", "Это круто", ["спорт", "плавание"]],
    ]
    events = {}
    max_count = 0
    for group in groups:
        events[group[0]] = 0
        for hobby in group[-1]:
            if hobby in hobbies_name:
                events[group[0]] += 1
        max_count = max(max_count, events[group[0]])

    for event in events.keys():
        if events[event] == max_count:
            result_list += event + "\n"
    return result_list

>>>>>>> origin/topando/chat_gpt
=======
>>>>>>> origin/Daryutin/frontChats
