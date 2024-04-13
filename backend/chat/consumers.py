import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"message": "Напиши рассказ о себе"}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data=json.dumps({"message": "Напиши рассказ о себе"}))


class ChatConsumerPath(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"message": "Опиши где ты находишься"}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data=json.dumps({"message": "Опиши где ты находишься"}))
