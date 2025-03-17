def search_by_instrument(applicants, instrument):
    return [applicant for applicant in applicants if applicant.instrument.lower() == instrument.lower()]


def sort_by_result(applicants):
    return sorted(applicants, key=lambda x: x.exam_result, reverse=True)
