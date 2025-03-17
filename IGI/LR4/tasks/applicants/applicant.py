class Applicant:
    def __init__(self, surname, instrument, exam_result):
        self.surname = surname
        self.instrument = instrument
        self.exam_result = exam_result

    def __str__(self):
        return f"Surname: {self.surname}, Instrument: {self.instrument}, Exam result: {self.exam_result}"

    def __repr__(self):
        return {
            "surname": self.surname,
            "instrument": self.instrument,
            "exam_result": self.exam_result
        }

    @staticmethod
    def from_dict(data):
        return Applicant(data["surname"], data["instrument"], data["exam_result"])

    def to_dict(self):
        """Convert object to dictionary for serialization."""
        return {
            "surname": self.surname,
            "instrument": self.instrument,
            "exam_result": self.exam_result
        }