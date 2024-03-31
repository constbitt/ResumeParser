import re
import datetime
from attributes_extractor.general_methods.data_extraction.dates_extractor import extract_date


def extract_birth(text):
    dates = extract_date(text)
    years = []
    for string in dates:
        matches = re.findall(r'\d{4}', string)
        for match in matches:
            years.append(int(match))
    if len(years) == 0:
        return None
    if (len(years) == 1 and datetime.datetime.now().year - years[0] >= 17) or (len(years) >= 2 and years[1] - years[0] >= 17):
        return dates[0]
    return None
