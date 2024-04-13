from rest_framework import serializers

from .models import *
from .utils import check_prompt


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageGPT
        fields = '__all__'

    def create(self, validated_data):
        answer = check_prompt(validated_data['text'])
        return answer
