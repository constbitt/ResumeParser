import csv


def save_to_csv(csv_path, cv_holder_name, birth, numbers, mails, links, education):
    data = [
        ["name", cv_holder_name],
        ["birth"] + birth,
        ["numbers"] + numbers,
        ["mails"] + mails,
        ["links"] + links,
        ["education"] + education
    ]
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

