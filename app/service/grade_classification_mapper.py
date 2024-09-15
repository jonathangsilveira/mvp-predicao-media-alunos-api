from app.model.grade import Grade


class GradeMapper:

    def map(self, classification: float) -> Grade:
        if classification < 1.0:
            return Grade.A
        elif classification < 2.0:
            return Grade.B
        elif classification < 3.0:
            return Grade.C
        elif classification < 4.0:
            return Grade.D
        else:
            return Grade.E