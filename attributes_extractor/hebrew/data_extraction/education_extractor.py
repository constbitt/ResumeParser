import re

from attributes_extractor.hebrew.data_extraction import matcher_extractor

education_pattern = [
    [{"IN": ["עוֹזֵר", "בוגר", "בוגרת", "סטודנט"]}, {"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"IN": ["במדאי", "במדעי"]},
     {"ANY": True},
     {"AND": "ו"}],

    [{"IN": ["עוֹזֵר", "בוגר", "בוגרת", "סטודנט"]}, {"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"AND": "ב"}, {"AND": "ו"}],

    [{"IN": ["עוֹזֵר", "בוגר", "בוגרת", "סטודנט"]}, {"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"AND": "ב"}, {"IN": ["ומדאי", "ומדעי"]},
     {"AND": "ה"}],

    [{"IN": ["עוֹזֵר", "בוגר", "בוגרת", "סטודנט"]}, {"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"IN": ["במדאי", "במדעי"]},
     {"ANY": True}],

    [{"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"IN": ["במדאי", "במדעי"]},
     {"ANY": True},
     {"AND": "ו"}],

    [{"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"IN": ["במדאי", "במדעי"]},
     {"ANY": True}],

    [{"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"AND": "ב"}, {"AND": "ו"}],

    [{"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"AND": "ב"}],

    [{"IN": ["תואר", "לתואר", "בתואר", "התואר"]},
     {"IN": ["מתקדם", "ראשון", "שני", "דוקטורט", "דוקטור", "הראשון", "השני"]}, {"AND": "ב"}, {"IN": ["ומדאי", "ומדעי"]},
     {"AND": "ה"}],

    [{"IN": ["סטודנט", "דוקטור", "דוקטורט", "בוגר", "בוגרת", ]}, {"AND": "ב"}, {"TEXT": "ומדאי"}, {"AND": "ה"}],

    [{"IN": ["סטודנט", "דוקטור", "דוקטורט", "בוגר", "בוגרת", ]}, {"AND": "ב"}, {"AND": "ו"}, {"AND": "ה"}],

    [{"IN": ["סטודנט", "דוקטור", "דוקטורט", "בוגר", "בוגרת", ]}, {"IN": ["במדאי", "במדעי"]}, {"ANY": True}],
]

universities = ["האוניברסיטה", "אוניברסיטה", "אוניברסיטת", "המכללה", "מכללה", "המכון", "מכון", "האקדמיה", "אקדמיה"]

university_pattern = [
    [{"IN": universities}, {"ANY": True}],

    [{"IN": universities}, {"ANY": True}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"IN": universities}, {"ANY": True}, {"AND": "ל"}, {"AND": "ו"}],

    [{"IN": universities}, {"ANY": True}, {"AND": "ל"}],

    [{"IN": universities}, {"TEXT": "של"}, {"ANY": True}],

    [{"IN": universities}, {"AND": "ל"}],

    [{"IN": universities}, {"AND": "ל"}, {"AND": "ו"}],

    [{"IN": universities}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"IN": universities}, {"AND": "ל"}, {"AND": "ב"}],

    [{"IN": universities}, {"AND": "ל"}, {"AND": "ו"}, {"AND": "ב"}],

    [{"IN": universities}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"AND": "ב"}],

    [{"IN": universities}, {"AND": "ל"}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"IN": universities}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"ANY": True}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"ANY": True}, {"AND": "ל"}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"ANY": True}, {"AND": "ל"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"AND": "ו"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "ספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"ANY": True}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"ANY": True}, {"AND": "ל"}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"ANY": True}, {"AND": "ל"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"AND": "ו"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"AND": "ב"}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"TEXT": "בית"}, {"TEXT": "הספר"}, {"AND": "ל"}, {"ANY": True}, {"AND": "ו"}, {"TEXT": "של"}, {"ANY": True}],

    [{"IN": universities}, {"TEXT": "תל"}, {"TEXT": "אביב"}],

    [{"IN": universities}, {"TEXT": "ראשון"}, {"TEXT": "לציון"}],

    [{"IN": universities}, {"TEXT": "בית"}, {"TEXT": "שאן"}],

    [{"IN": universities}, {"TEXT": "סנט"}, {"TEXT": "פטרסבורג"}],

]


def extract_something(text, pattern):
    educations = matcher_extractor.extract_matching(text, pattern)
    list_educations = []
    for education in educations:
        description = ""
        for part in education:
            description += " " + part
        list_educations.append(description)

    return list_educations


def check_substrings_distance(text, substring1, substring2):
    index1 = text.find(substring1)
    index2 = text.find(substring2)
    if index1 == -1 or index2 == -1:
        return -1
    start1 = index1
    end1 = start1 + len(substring1)
    start2 = index2
    end2 = start2 + len(substring2)
    if start1 >= end2:
        distance = abs(start1 - end2)
    else:
        distance = abs(start2 - end1)
    if distance < 10:
        return True
    return False


def extract_education(text):
    educations = extract_something(text, education_pattern)
    unis = extract_something(text, university_pattern)
    educations_list = []
    for university in unis:
        for edu in educations:
            if check_substrings_distance(text, edu, university):
                edu = edu + ", " + university
                educations_list.append(edu)
    return educations_list
