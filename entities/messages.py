messages = {"message":"limit error message",
            "default":"Special Message"}

def get_massages():
    global messages
    return messages

def set_message(message):
    global messages
    messages['message'] = message
    return

