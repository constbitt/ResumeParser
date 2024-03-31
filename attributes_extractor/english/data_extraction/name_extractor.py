import re

from spacy.matcher import Matcher


def extract_name(text, nlp):
    name1 = re.findall(r"\b[A-Za-z]+\b", text)[0] + " " + re.findall(r"\b[A-Za-z]+\b", text)[1]
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break
    if name1 != name:
        return name1
    return name

