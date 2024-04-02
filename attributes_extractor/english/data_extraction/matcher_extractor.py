from spacy.matcher import Matcher
from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_matching(text, nlp, patterns, i, stop_words=None):
    if stop_words is None:
        stop_words = []
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    for pattern in patterns:
        matcher.add(i, [pattern])
    matches = matcher(doc)
    matching_list = []
    for match_id, start, end in matches:
        matched_span = doc[start:end]
        if match_id == i:
            matching_list.append(matched_span.text)

    for stop_word in stop_words:
        matching_list = list(filter(lambda s: stop_word not in s.lower(), matching_list))

    list_cleaner = ListCleaner(matching_list)
    matching_list = list_cleaner.clean_words(matching_list)
    return matching_list

