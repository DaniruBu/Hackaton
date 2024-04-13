import json
import time

from channels.generic.websocket import WebsocketConsumer

from chat.utils import check_prompt

from chat.models import MessageGPT


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"message": "Привет, я могу отвечать на твои вопросы\nДавай ты расскажешь о себе"}))

    def disconnect(self, close_code):
        MessageGPT.objects.all().delete()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
        answer = check_prompt(message)
        self.send(text_data=json.dumps({"message": answer}))


