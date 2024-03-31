import re


def custom_splitter(text):
    words = re.split(r'\s+|[,.;!?]|\n', text)
    words = [word for word in words if word]
    return words