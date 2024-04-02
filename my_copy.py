import csv
import pyperclip


def copy(cv_holder_name, birth, numbers, mails, links, education):
    data = [
        ["name", cv_holder_name],
        ["birth"] + birth,
        ["numbers"] + numbers,
        ["mails"] + mails,
        ["links"] + links,
        ["education"] + education
    ]
    csv_data = '\n'.join([','.join(row) for row in data])
    pyperclip.copy(csv_data)

