import time

from rest_framework import serializers, viewsets

from .models import *
from .utils import check_prompt, get_prompt_message, get_hobby, sorting_event


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

class GetOptimalRouteChatViewSet(viewsets.ModelViewSet):
    class Meta:
        pass