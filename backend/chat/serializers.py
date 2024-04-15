import queue

from rest_framework import serializers

from .chat_gpt import generate_response
from .models import *


class ppppppp:
    def bebebe(data, v, s, end):
        array = []
        parent = []
        used_len = []

        for i in range(v + 1):
            array.append([])
            used_len.append(999999999999999999999)
            parent.append(99999999999999999999)

        for i in data:
            array[i[0]].append([i[1], i[2], i[3]])

        q = queue.Queue()
        used_len[s] = 0
        q.put(s)

        while not q.empty():
            now = q.get()
            for i in array[now]:
                if used_len[now] + i[1] < used_len[i[0]]:
                    used_len[i[0]] = used_len[now] + i[1]
                    parent[i[0]] = now
                    q.put(i[0])

        now = end
        ret = []
        while now != s:
            for i in array[now]:
                if i[0] == parent[now]:
                    ret.append(i[2])
            now = parent[now]

        return list(reversed(ret))


class ChatSerializer(serializers.Serializer):
    description = serializers.CharField()

    def save(self, **kwargs):
        text = None
        obj = StateMessanger.objects.get_or_create()[0]
        if obj.state == 0:
            text = "Составьте о себе короткий текст"
        if obj.state == 1:
            prompt = get_check_info_prompt(self.validated_data['description'])
            messages = get_request_chat_gpt(prompt, 'user')
            if int(generate_response(messages)):
                prompt = get_info_prompt(self.validated_data['description'])
                messages = get_request_chat_gpt(prompt, 'user')
                print(generate_response(messages))
            else:
                text = "Составьте о себе короткий текст"
        obj.save()
        return text


class GetOptimalRouteChatSerializer(serializers.Serializer):
    description = serializers.CharField()

    def save(self, **kwargs):
        text = None
        obj = State.objects.get_or_create(pk=1)
        if obj[0].state == 0:
            text = "Введите где вы находитесь"
        if obj[0].state == 1:
            description = self.validated_data['description']
            obj[0].start_point = description
            text = "Это то где вы находитесь: " + description + "?"
        if obj[0].state == 2:
            prompt = get_prompt_check_point(self.validated_data['description'])
            messages = get_request_chat_gpt(prompt, 'user')
            if int(generate_response(messages)):
                text = "Введите куда вам нужно"
            else:
                text = "Введите где вы находитесь"
                obj[0].state -= 2
        if obj[0].state == 3:
            description = self.validated_data['description']
            obj[0].end_point = description
            text = "Это то куда вам надо: " + description + "?"
        if obj[0].state == 4:
            prompt = get_prompt_check_point(self.validated_data['description'])
            messages = get_request_chat_gpt(prompt, 'user')
            if int(generate_response(messages)):
                pass
            else:
                text = "Введите куда вам нужно"
                obj[0].state -= 2

        obj[0].state += 1
        obj[0].save()
        return text


def get_prompt_check_point(message):
    text = f"Если в сообщении '{message}' полное согласие, ответь 1 иначе 0"
    return text


def get_request_chat_gpt(prompt, role):
    messages = [{
        'role': role,
        'content': prompt
    }]
    return messages


def get_check_info_prompt(message):
    text = f"Если сообщение '{message}' это  информация о пользователе или о его увлечениях, ответь 1 иначе 0"
    return text


def get_info_prompt(message):
    text = (f"'{message}' - проанализируй это сообщение по виду:"
            f"Если в нем есть имя пользователя отправь JSON вида 'name': name, иначе JSON вида 'name': null"
            f"Если в нем есть хобби пользователя отправь JSON вида 'hobby': [hobby, hobby], иначе 'hobby': null"
            f"Если в нем есть то чем пользователь хотел бы заниматься отправь JSON вида 'dream': [dream, dream], иначе 'dream': null"
            )
    return text
