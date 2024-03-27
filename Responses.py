from datetime import datetime

def sample_responses(input_text):
    user_messege = str(input_text).lower()
    if user_messege in ('hello', "hi", 'sup'):
        return 'Hello, I am bot'

    if user_messege in ('who are you?'):
        return 'I am a bot'

    return "I don't understand you"
