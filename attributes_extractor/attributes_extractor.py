import spacy
from attributes_extractor.english.english_extractor import extract_english
from attributes_extractor.general_methods.text_extractor import TextExtractor
from attributes_extractor.hebrew.hebrew_extractor import extract_hebrew


def extract_attributes(file_path, language):
    extractor = TextExtractor(file_path)
    cv_text = extractor.extract_text(file_path)
    cv_holder_name = None
    birth = None
    numbers = None
    mails = None
    links = None
    education = None
    print(cv_text)
    nlp = spacy.load("en_core_web_sm")
    if language == "hebrew":
        nlp.add_pipe("span_marker", config={"model": "iahlt/span-marker-xlm-roberta-base-nemo-mt-he"})
        cv_holder_name, birth, numbers, mails, links, education = extract_hebrew(cv_text, nlp)
    elif language == "english":
        cv_holder_name, birth, numbers, mails, links, education = extract_english(cv_text, nlp)
        print(cv_holder_name, "\n", birth, "\n", numbers, "\n", mails, "\n", links, "\n", education)
    else:
        return None
    return cv_holder_name, birth, numbers, mails, links, education


