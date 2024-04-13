import json

import requests
from chat.chat_gpt import get_prompt_message, add_message_chat_gpt, generate_response
from chat.models import CountMessages
from config.settings import USER
