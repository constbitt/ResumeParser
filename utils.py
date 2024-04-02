
def to_csv_format(data, delimiter):
    cv_holder_name = data.get('cv_holder_name')
    birth = data.get('birth')
    numbers = data.get('numbers')
    mails = data.get('mails')
    links = data.get('links')
    education = data.get('education')

    csv_data = f"cv_holder_name{delimiter}{cv_holder_name}\n"
    csv_data += f"birth{delimiter}{birth}\n"

    if numbers:
        csv_data += f"numbers{delimiter}{delimiter.join(map(str, numbers))}\n"

    if mails:
        csv_data += f"mails{delimiter}{delimiter.join(map(str, mails))}\n"

    if links:
        csv_data += f"links{delimiter}{delimiter.join(map(str, links))}\n"

    if education:
        csv_data += f"education{delimiter}{delimiter.join(map(str, education))}\n"

    return csv_data

