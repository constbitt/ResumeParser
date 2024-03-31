import re

from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_mail(text):
    mails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    list_cleaner = ListCleaner(mails)
    mails = list_cleaner.clean_words(mails)
    return mails
