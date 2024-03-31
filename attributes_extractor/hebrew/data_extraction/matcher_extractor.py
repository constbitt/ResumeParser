from attributes_extractor.general_methods.auxiliary_methods.custom_matcher import CustomMatcher
from attributes_extractor.general_methods.auxiliary_methods.custom_splitter import custom_splitter
from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_matching(text, pattern):
    matcher = CustomMatcher(pattern)
    words = custom_splitter(text)
    matches = matcher.match(words)
    matching_list = []
    for start, end in matches:
        matching_list.append(words[start:end])
    list_cleaner = ListCleaner(matching_list)
    matching_list = list_cleaner.clean_words(matching_list)
    return matching_list
