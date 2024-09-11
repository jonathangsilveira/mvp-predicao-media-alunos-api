from app.model.grade import Grade


class GradeMapper:

    def map(self, classification: int) -> Grade:
        grades = {
            0: Grade.A,
            1: Grade.B,
            2: Grade.C,
            3: Grade.D,
            4: Grade.E
        }
        return grades[classification]