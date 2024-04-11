import re
from attributes_extractor.english.data_extraction import matcher_extractor

languages = [
    "hebrew", "english", "arabic", "german", "russian", "spanish", "greek", "japanese", "chinese", "italian",
    "portuguese", "dutch", "swahili", "persian", "aramaic", "sanskrit", "filipino", "finnish", "indonesian",
    "french", "ukrainian", "belarusian",
    "עברית", "אנגלית", "ערבית", "קריס", "רוסית", "סרבית", "גרמנית", "יוונית", "יפנית", "סינית", "איטלקית",
    "פורטוגזית", "הולנדית", "", "סווהילי", "פרסית", "ארמית", "סנסקריט", "פיליפיני", "פינית", "אינדונזית",
    "צרפתית", "בלארוסית", "", "אוקראינית",
]

language_pattern = [
    [{"LOWER": {"IN": languages}}]
]

stop_words = []


def extract_languages(text, nlp):
    langs = matcher_extractor.extract_matching(text, nlp, language_pattern, 3, stop_words)
    languages_list = ""
    for i, language in enumerate(langs):
        if i == 0:
            languages_list += language
        else:
            languages_list += ", " + language
    return languages_list
