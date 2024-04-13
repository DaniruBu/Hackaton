import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MessageGPT
from .utils import check_prompt

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Привет, я могу отвечать на твои вопросы\nДавай ты расскажешь о себе"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat", self.channel_name)
        await MessageGPT.objects.all().delete()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.send(text_data=json.dumps({"message": message}))
        answer = check_prompt(message)
        await self.send(text_data=json.dumps({"message": answer}))
