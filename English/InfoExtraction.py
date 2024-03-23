import PyPDF2
import spacy
from spacy.matcher import Matcher
from GeneralMethods.Extraction import extract_emails
from GeneralMethods.Extraction import extract_links
from GeneralMethods.Extraction import extract_phone_numbers
from GeneralMethods.Extraction import extract_dates

nlp = spacy.load("en_core_web_sm")
education_pattern = [
    [{"LOWER": {"IN": ["bachelor's", "bachelor", "bs"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],
    [{"LOWER": {"IN": ["master's", "master", "ms"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],
    [{"LOWER": {"IN": ["doctoral", "phd", "ph.d"]}}, {"IS_PUNCT": True}, {"LOWER": "degree"}],
    [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}],
    [{"LOWER": "bachelor"}, {"LOWER": "of", "OP": "?"}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],
    [{"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}, {"LOWER": ",", "OP": "?"}, {"LOWER": {"IN": ["student", "bachelor's", "bachelor", "bs", "doctoral", "doctor's", "doctor", "phd", "ph.d", "master's", "master", "ms", "mba", "jd", "md", "associate"]}}],
    [{"LOWER": "master"}, {"LOWER": "of"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}],
    [{"LOWER": "master"}, {"LOWER": "of", "OP": "?"}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],
    [{"LOWER": "doctor"}, {"LOWER": "of"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"LOWER": "in"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}],
    [{"LOWER": "dpctor"}, {"LOWER": "of", "OP": "?"}, {"LOWER": "in", "OP": "?"}, {"LOWER": ",", "OP": "?"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],
    [{"LOWER": {"IN": ["bachelor's", "bachelor", "bs", "doctoral", "phd", "ph.d", "master's", "master", "ms", "mba", "jd", "md", "associate"]}}, {"LOWER": "degree", "OP": "?"}, {"LOWER": "in"}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}}, {"POS": {"IN": ["NNS", "NNPS", "PROPN", "NOUN"]}, "OP": "?"}],
]

matcher = Matcher(nlp.vocab)
for pattern in education_pattern:
    matcher.add(1, [pattern])

def extract_entities(text):
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

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def extract_cv_holder_name(text):
    doc = nlp(text)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break
    if name is None:
        for match_id, start, end in matcher(doc):
            if match_id == 1:
                name = doc[start - 1].text + " " + doc[start].text
                break
    return name


def extract_education(text):
    doc = nlp(text)
    matches = matcher(doc)
    print(doc)
    educations = []
    for match_id, start, end in matches:
        matched_span = doc[start:end]
        if match_id == 1:
            educations.append(matched_span.text)
    return educations

#pdf_path = r"C:\Users\Acer ASPIRE 5\OneDrive\Рабочий стол\погром\курсовая\реальная курсовая\cvdet\pdfs\cv_10.pdf"
#cv_text = extract_text_from_pdf(pdf_path)
#cv_text = ("sdkjjf 17.04.2001 name Ann Juder dkjfkjgjk +79998876529 hello student ffklklf call me i am alive \n skdfjk ms.biderina@mail.ru\n https://chat.openai.com/c/80790c01-e227-40bf-ba92-833bc9c4ebc8 fhdhgshga: Computer Science, student, University of Oxford, 2007")
#print("Extracted Text:")
#print(cv_text.lower())

def extract_atributes(cv_text):
    #cv_text = ("sdkjjf 17.04.2001 name Ann Juder dkjfkjgjk +79998876529 hello student ffklklf call me i am alive \n skdfjk ms.biderina@mail.ru\n https://chat.openai.com/c/80790c01-e227-40bf-ba92-833bc9c4ebc8 fhdhgshga: Computer Science, student, University of Oxford, 2007")
    entities = extract_entities(cv_text)
    cv_holder_name = extract_cv_holder_name(cv_text)
    phone_numbers = extract_phone_numbers(cv_text)
    emails = extract_emails(cv_text)
    links = extract_links(cv_text)
    dates = extract_dates(cv_text)
    educations = extract_education(cv_text)
    return cv_holder_name, phone_numbers, emails, links

'''
print("\nName:", cv_holder_name)
print("Entities:", entities)
print("Phone numbers:", phone_numbers)
print("Emails:", emails)
print("Links:", links)
print("Education:", educations)
print("Dates:", dates)

'''