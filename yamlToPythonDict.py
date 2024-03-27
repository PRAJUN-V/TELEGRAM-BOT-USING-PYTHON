import yaml
import re

def load_conversations(filename):
    with open(filename, "r") as file:
        conversations = yaml.safe_load(file)
    return conversations

def clean_key(key):
    # Remove special characters and extra spaces from the key
    cleaned_key = re.sub(r'[^a-zA-Z\s]', '', key)  # Remove non-alphabetic characters
    cleaned_key = re.sub(r'\s+', ' ', cleaned_key).strip()  # Remove extra spaces
    return cleaned_key.lower()

def conversations_to_dict(conversations):
    qa_pairs = {}
    for conversation in conversations:
        question, answer = conversation[0], conversation[1]
        cleaned_question = clean_key(question)
        qa_pairs[cleaned_question] = answer
    return qa_pairs

conversations = load_conversations("computers.yml")
qa_pairs = conversations_to_dict(conversations["conversations"])

print(qa_pairs)
responses = qa_pairs
