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
    doc = nlp(name1.lower())
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            return name1
    if name1 != name and text.find(name) < len(text) // 20:
        return name
    return None

