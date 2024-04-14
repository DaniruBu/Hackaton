import queue
import time

from rest_framework import serializers

from .chat_gpt import generate_response
from .models import *
from .utils import check_prompt, get_prompt_message, get_hobby, sorting_event, get_analytical_prompt, get_es_prompt


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


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageGPT
        fields = '__all__'

    def save(self, **kwargs):
        if MessageGPT.objects.all().count() == 1 and check_prompt(self.validated_data['text'], 1) == '0':
            MessageGPT.objects.all().delete()
            MessageGPT.objects.create(
                role="system",
                text=get_prompt_message(0)
            ).save()
            return "Неверный ввод"

        MessageGPT.objects.create(
            role="user",
            text=self.validated_data['text']
        ).save()
        time.sleep(3)
        answer = check_prompt(self.validated_data['text'], 0)
        MessageGPT.objects.create(
            role="assistant",
            text=answer
        ).save()
        if get_hobby(answer):
            result = sorting_event()
            return result
        else:
            return answer


state = 0
start_point = None
start_point_id = 0
end_point = None
end_point_id = 0


class GetOptimalRouteChatSerializer(serializers.Serializer):
    description = serializers.CharField()

    def save(self, **kwargs):
        global state, start_point_id, end_point_id
        text = None

        if state == 0:
            text = "Опишите где вы находитесь"
        elif state == 1:
            text = "Это то где вы находитесь: "
        elif state == 2:
            text = "Опишите куда вам надо"
        elif state == 3:
            text = "Это то куда вам надо:  "

        RequestGetOptimalRouteChat.objects.create(
            text=text
        )

        if state % 2 != 0:
            all_points = [
                {
                    "id": 1,
                    "description": "Главный вход"
                },
                {
                    "id": 2,
                    "description": "Столовая"
                }, {
                    "id": 3,
                    "description": "Окно"
                },
                {
                    "id": 4,
                    "description": "Раздевалка"
                },

            ]
            messages = [{
                'role': "system",
                'content': get_analytical_prompt(self.validated_data['description'], all_points)}]
            answer = generate_response(messages)
            text += str(answer['id'])
            state += 1
            if state == 1:
                start_point_id = int(answer['id'])
            else:
                end_point_id = int(answer['id'])
        else:
            messages = [{
                'role': "system",
                'content': get_es_prompt(self.validated_data['description'])
            }]
            if generate_response(messages):
                state += 1
                if state == 5:
                    res = []
                    vetks = Vetka.objects.all()
                    for vetk in vetks:
                        res.append([vetk.start, vetk.end, vetk.len, vetk.description])
                    obj = ppppppp()
                    k = obj.bebebe(res, 1009999, start_point_id, end_point_id)
                    for i in k:
                        print(i)
        return text
