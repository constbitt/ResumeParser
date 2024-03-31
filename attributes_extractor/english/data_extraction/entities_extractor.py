def extract_entities(nlp, text):
    doc = nlp(text)
    entities = set()
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities.add(ent.text)
    for token in doc:
        if token.pos_ == "PROPN" and token.text.istitle():
            entity = token.text
            while True:
                next_token = token.nbor()
                if next_token.pos_ == "PROPN" and next_token.text.istitle():
                    entity += " " + next_token.text
                    token = next_token
                else:
                    break
            entities.add(entity)

    return list(entities)