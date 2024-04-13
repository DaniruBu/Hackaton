from chat.chat_gpt import get_prompt_message, add_message_chat_gpt, generate_response


def set_info_student(message, count):
    prompt_message = get_prompt_message(count)
    messages = [{
        "role": 'system',
        "content": prompt_message['prompt']
    }]
    messages.append(add_message_chat_gpt(message, 'user'))
    return generate_response(messages)
