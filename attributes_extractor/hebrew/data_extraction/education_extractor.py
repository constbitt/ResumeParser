from attributes_extractor.hebrew.data_extraction import matcher_extractor

education_pattern = [
    [{"TEXT": "תואר"}, {"IN": ["מתקדם", "ראשון", "במדעי"]}, {"ANY": True, "OP": "?"}],
    [{"TEXT": "תואר"}, {"IN": ["מתקדם", "ראשון"]}, {"TEXT": "במדעי"}, {"ANY": True, "OP": "?"}],
    [{"TEXT": "דוקטור"}, {"TEXT": "למדעי"}, {"ANY": True, "OP": "?"}],
    [{"TEXT": "סטודנט"}, {"TEXT": "התואר"}, {"IN": ["מתקדם", "ראשון"]}, {"TEXT": "במדעי"}, {"ANY": True, "OP": "?"}],
    [{"TEXT": "סטודנט"}, {"TEXT": "התואר"}, {"IN": ["מתקדם", "ראשון"]}, {"ANY": True, "OP": "?"}],
    [{"IN": ["מדעי", "לימודי", "תואר"]}, {"ANY": True, "OP": "?"}],
    [{"TEXT": "בוגר"}, {"TEXT": "מדעי"}, {"ANY": True}],
    [{"TEXT": "פוסט"}, {"TEXT": "דוקטורט"}, {"TEXT": "במדעי"}, {"ANY": True}],
    [{"TEXT": "פוסט"}, {"TEXT": "דוקטורט"}, {"ANY": True}],
]


def extract_education(text):
    educations = matcher_extractor.extract_matching(text, education_pattern)
    return educations
