from tasks.applicants.applicant import Applicant
from tasks.applicants.serializers.csv_serializer import save_to_csv, load_from_csv
from tasks.applicants.serializers.pickle_serializer import save_to_pickle
from tasks.applicants.sorters.sorters_funcs import search_by_instrument, sort_by_result
from tasks.applicants.decors.handle_exception import handle_errors
from tasks.applicants.inputs.get_input import get_input
from tasks.applicants.inputs.get_valid_int import get_valid_int


@handle_errors
def main():
    filename_csv = 'applicants.csv'
    filename_pkl = 'applicants.pkl'

    applicants = load_from_csv(filename_csv)

    while True:
        print("\nEnter applicant details (or type '0' to exit):")

        surname = get_input("Enter surname: ")
        instrument = get_input("Enter musical instrument: ")
        exam_result = get_valid_int("Enter exam result (1-100): ", 1, 100)

        applicants.append(Applicant(surname, instrument, exam_result))

        if get_input("Do you want to add another applicant? (y/n): ").lower() != 'y':
            break

    save_to_csv(applicants, filename_csv)
    save_to_pickle(applicants, filename_pkl)

    print("\nSearch applicants by instrument:")
    instrument_to_search = get_input("Enter instrument: ")
    found_applicants = search_by_instrument(applicants, instrument_to_search)

    if found_applicants:
        print(f"Applicants found for instrument {instrument_to_search}:")
        for applicant in found_applicants:
            print(f"Surname: {applicant.surname}, Instrument: {applicant.instrument}, Exam result: {applicant.exam_result}")
    else:
        print("No applicants found for this instrument.")

    print("\nApplicants sorted by exam result:")
    for applicant in sort_by_result(applicants):
        print(f"Surname: {applicant.surname}, Instrument: {applicant.instrument}, Exam result: {applicant.exam_result}")


if __name__ == "__main__":
    main()
