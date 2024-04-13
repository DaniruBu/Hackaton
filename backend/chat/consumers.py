import json

from channels.generic.websocket import WebsocketConsumer
from chat.utils import create_room, get_count_user
from chat.utils import set_info_student

from chat.utils import count_add_message, get_next_message

from chat.utils import get_len_prompts


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        create_room()
        self.accept()
        self.send(text_data=json.dumps({"message": "Напишите свои хобби"}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        count = get_count_user()
        if count < get_len_prompts():
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]
            self.send(text_data=json.dumps({"message": message}))
            answer = set_info_student(message, count)
            self.send(text_data=json.dumps({"message": answer}))
            count_add_message()
            if count + 1 < get_len_prompts():
                start_message = get_next_message(count + 1)
                self.send(text_data=json.dumps({"message": start_message}))
