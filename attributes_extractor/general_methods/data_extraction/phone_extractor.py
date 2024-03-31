import re

from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_phone(text):
    phones = []
    patterns = [
        r'(?:(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b',
        r'\(\d{3}\) \d{3} \u2013 \d{4}',
        r'\+\d{2} \(\d{1}\)\d{2} \d{4} \d{4}',
        r'\+\d\s\(\d{3}\)\s\d{3}-\d{4}',
        r'\+\d\s\(\d{3}\)\s\d{3} -\d{4}'
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            phones.append(match)
    list_cleaner = ListCleaner(phones)
    phones = list_cleaner.clean_words(phones)
    return phones
