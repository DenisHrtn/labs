import csv

from tasks.applicants.applicant import Applicant


def save_to_csv(applicants, filename='applicants.csv'):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['surname', 'instrument', 'exam_result'])
        writer.writeheader()

        for applicant in applicants:
            writer.writerow(applicant.to_dict())


def load_from_csv(filename='applicants.csv'):
    applicants = []

    try:
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                row['exam_result'] = int(row['exam_result'])
                applicants.append(Applicant.from_dict(row))
    except FileNotFoundError:
        print("File not found")

    return applicants
