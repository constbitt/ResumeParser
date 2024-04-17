def extract_name(text, nlp):
    #doc = nlp(text)
    name = None
    #for ent in doc.ents:
    #    if ent.label_ == 'PER':
    #        name = ent.text
    #        break
    if name is None:
        name = text.split()[0] + ' ' + text.split()[1]
    return name
