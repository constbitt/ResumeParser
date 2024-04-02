import re
from attributes_extractor.english.data_extraction import matcher_extractor

degrees = ["bachelor", "master", "ba", "ma", "bs", "ms", "doctor", "phd", "ph.d", "mba", "bachelor's", "master's",
           "bachelor's", "bachelor", "bs", "doctoral", "phd", "ph.d", "master's", "master", "ms", "mba", "jd",
           "md", "associate", "ba", "ma", "student", "bachelor's", "bachelor", "bs", "doctoral", "doctor's", "doctor",
           "phd", "ph.d",
           "master's", "master", "ms", "mba", "jd", "md", "associate", "msc"]

parts = ["NNS", "NNPS", "PROPN", "NOUN"]

universities = ["university", "college", "school", "institute", "academy", "center", "department", "campus"]

stop_words = ["education", "experience"]

education_pattern = [
    [{"LOWER": {"IN": degrees}}, {"LOWER": "of"}, {"POS": {"IN": parts}}, {"POS": {"IN": parts}, "OP": "?"}, {"LOWER": "in"},
     {"POS": {"IN": parts}}, {"POS": {"IN": parts}, "OP": "?"}],

    [{"LOWER": {"IN": degrees}}, {"LOWER": {"IN": ["of", "in"]}}, {"POS": {"IN": parts}}, {"POS": {"IN": parts}, "OP": "?"}],

    [{"POS": {"IN": parts}, "OP": "?"}, {"POS": {"IN": parts}}, {"LOWER": {"IN": degrees}}],

    [{"POS": {"IN": parts}, "OP": "?"}, {"POS": {"IN": parts}}, {"LOWER": ","}, {"LOWER": {"IN": degrees}}],
]


university_pattern = [
    [{"LOWER": {"IN": universities}}, {"LOWER": "of"}, {"POS": {"IN": parts}}, {"POS": {"IN": parts}, "OP": "?"}],

    [{"POS": {"IN": parts}, "OP": "?"}, {"POS": {"IN": parts}, "OP": "?"}, {"LOWER": {"IN": universities}}],

    [{"POS": {"IN": parts}}, {"LOWER": {"IN": universities}}, {"LOWER": "of"}, {"POS": {"IN": parts}}, {"POS": {"IN": parts}, "OP": "?"}],
]


def extract_education(text, nlp):
    educations = matcher_extractor.extract_matching(text, nlp, education_pattern, 1, stop_words)

    unis = matcher_extractor.extract_matching(text, nlp, university_pattern, 2, stop_words)
    for university in unis:
        for i in range(len(educations)):
            if check_substrings_distance(text, university, educations[i]):
                educations[i] = educations[i] + ", " + university
    return educations


def check_substrings_distance(string, substring1, substring2):
    pattern = re.compile(r"\b{}\b(?:\W+\w+){{0,10}}\W+{}\b|\b{}\b(?:\W+\w+){{0,10}}\W+{}\b".format(
        substring1, substring2, substring2, substring1))
    if re.search(pattern, string):
        return True
    else:
        return False