from attributes_extractor.english.data_extraction import matcher_extractor

education_pattern = [
    [{"LOWER": {"IN": ["bachelor's", "bachelor", "bs"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],

    [{"LOWER": {"IN": ["master's", "master", "ms"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],
    [{"LOWER": {"IN": ["doctoral", "phd", "ph.d"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],

    [{"LOWER": {"IN": ["bachelor", "master", "ba", "ma", "bs", "ms", "doctor", "phd", "ph.d", "mba"]}}, {"LOWER": "of"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"LOWER": {"IN": ["bachelor", "master", "ba", "ma", "bs", "ms", "doctor", "phd", "ph.d", "mba"]}}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}, {"LOWER": ",", "OP": "?"}, {"LOWER": {
        "IN": ["student", "bachelor's", "bachelor", "bs", "doctoral", "doctor's", "doctor", "phd", "ph.d",
               "master's", "master", "ms", "mba", "jd", "md", "associate", "msc"]}}],

    [{"LOWER": "master"}, {"LOWER": "of"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}],

    [{"LOWER": "master"}, {"LOWER": "of", "OP": "?"}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"LOWER": "doctor"}, {"LOWER": "of"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}],

    [{"LOWER": "dpctor"}, {"LOWER": "of", "OP": "?"}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}},
     {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"LOWER": {
        "IN": ["bachelor's", "bachelor", "bs", "doctoral", "phd", "ph.d", "master's", "master", "ms", "mba", "jd",
               "md", "associate", "ba", "ma"]}}, {"LOWER": "degree", "OP": "?"}, {"LOWER": "in"},
        {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}},
        {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"LOWER": {
        "IN": ["bachelor's", "bachelor", "bs", "doctoral", "phd", "ph.d", "master's", "master", "ms", "mba", "jd",
               "md", "associate", "ba", "ma"]}}, {"LOWER": "degree", "OP": "?"}, {"LOWER": "in"},
        {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "and", "OP": "?"},
        {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],

    [{"LOWER": {
        "IN": ["student", "bachelor's", "bachelor", "bs", "doctoral", "doctor's", "doctor", "phd", "ph.d",
               "master's", "master", "ms", "mba", "jd", "md", "associate", "msc", "ba", "ma"]}}]
]


def extract_education(text, nlp):
    educations = matcher_extractor.extract_matching(text, nlp, education_pattern, 1)
    educations = list(filter(lambda s: 'education' not in s.lower(), educations))
    return educations


