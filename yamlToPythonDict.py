import yaml
import re
import os

def load_conversations_from_files(file_list):
    all_conversations = []
    for filename in file_list:
        file_path = os.path.join("ymlFiles", filename)  # Adjust the folder name here
        with open(file_path, "r") as file:
            conversations = yaml.safe_load(file)
            all_conversations.extend(conversations["conversations"])
    return all_conversations

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

# List of YAML files
yaml_files = ["computers.yml", "science.yml", "humor.yml", "ai.yml"]  # Add more filenames as needed

conversations = load_conversations_from_files(yaml_files)
qa_pairs = conversations_to_dict(conversations)

a = {
    'start': 'How can I help you?',
    "hi": "Hello!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye!",
    "i love you": "Love you too...",
    "whats your name": "I'm a chatbot created by ChatGPT.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "do you like pizza?": "Yes, I love pizza!",
    "what's the meaning of life?": "The meaning of life is a philosophical question with no single answer.",
    "can you help me with my homework?": "I can provide assistance, but I encourage you to learn and understand the concepts yourself.",
    "where do you live?": "I exist in the digital realm, roaming the internet!",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    # Add more responses as needed
}

print(qa_pairs)
qa_pairs.update(a)
responses = qa_pairs
