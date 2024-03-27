import yaml
import re
import os

def load_conversations_from_files(file_list):
    all_conversations = []
    for filename in file_list:
        with open(filename, "r") as file:
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

print(qa_pairs)
responses = qa_pairs
