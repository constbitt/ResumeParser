import re

from attributes_extractor.general_methods.auxiliary_methods.list_cleaner import ListCleaner


def extract_date(text):
    dates = []
    patterns = [
        r'(?<!\d)(\d{4}-\d{2}-\d{2})(?!\d)',
        r'(?<!\d)(\d{4}[.-]\d{2}[.-]\d{2})(?!\d)',
        r'(?<!\d)(\d{4}/\d{2}/\d{2})(?!\d)',
        r'(?<!\d)([a-zA-Z]+\s\d{1,2},\s\d{4})(?!\d)',
        r'(?<!\d)(\d{2}/\d{2}/\d{2})(?!\d)',
        r'(?<!\d)(\d{2}[-.]\d{2}[-.]\d{4})(?!\d)',
        r'(?<!\d)(\d{2}/\d{2}/\d{4})(?!\d)',
        r'(?<!\d)(\d{2}[-.]\d{2}[-.]\d{2})(?!\d)',
        r'\d{1,2}/(?:January|February|March|April|May|June|July|August|September|October|November|December)/\d{4}',
        r'(?<!\d)(\d{1,2}\s(?:ינואר|פברואר|מרץ|אפריל|מאי|יוני|יולי|אוגוסט|ספטמבר|אוקטובר|נובמבר|דצמבר)\s\d{4})(?!\d)',
        r'(?<!\d)(\d{1,2}\sב(?:ינואר|פברואר|מרץ|אפריל|מאי|יוני|יולי|אוגוסט|ספטמבר|אוקטובר|נובמבר|דצמבר)\s\d{4})(?!\d)',
        r'(?<!\d)(\d{4}\s(?:ינואר|פברואר|מרץ|אפריל|מאי|יוני|יולי|אוגוסט|ספטמבר|אוקטובר|נובמבר|דצמבר)\s\d{1,2})(?!\d)',
        r'(?<!\d)(\d{4}\sב(?:ינואר|פברואר|מרץ|אפריל|מאי|יוני|יולי|אוגוסט|ספטמבר|אוקטובר|נובמבר|דצמבר)\s\d{1,2})(?!\d)'
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            dates.append(match)

    dates = [date for date in dates if not (re.match(r'\d', text[text.find(date)-1]) or re.match(r'\d', text[text.find(date)+len(date)]))]

    list_cleaner = ListCleaner(dates)
    dates = list_cleaner.clean_words(dates)
    return dates
