import re

from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_link(text):
    links = re.findall(r'(https?://\S+)', text)
    links.extend(re.findall(r'ftp://\S+', text))
    links.extend(re.findall(r'\b\w+\.com/\S+', text))
    list_cleaner = ListCleaner(links)
    links = list_cleaner.leave_almost_subsets(links)
    return links
