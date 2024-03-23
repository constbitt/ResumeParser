import re
def extract_phone_numbers(text):
    phone_number_pattern = r'(?:(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b'
    phone_numbers = re.findall(phone_number_pattern, text)
    return phone_numbers


def extract_emails(text):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails


def extract_links(text):
    links = re.findall(r'(https?://\S+)', text)
    return links


def extract_dates(text):
    dates = re.findall(r'\d{2}[-.]\d{2}[-.]\d{4}', text)
    dates.append(re.findall(r'\d{4}-\d{2}-\d{2}', text))
    dates.append(re.findall(r'[a-zA-Z]+\s\d{1,2},\s\d{4}', text))
    dates.append(re.findall(r'\d{2}/\d{2}/\d{2}', text))
    return dates
