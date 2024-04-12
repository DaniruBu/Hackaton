import json

from channels.generic.websocket import WebsocketConsumer

from chat.utils import get_answer_ai


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        get_answer_ai(message)
        self.send(text_data=json.dumps({"message": message}))