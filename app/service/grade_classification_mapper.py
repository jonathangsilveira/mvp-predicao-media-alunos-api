
from app.model.grade_classification import GradeClassification

def to_grade_classification(classification: int) -> GradeClassification:
    if classification == 0:
        return GradeClassification.A
    elif classification == 1: 
        return GradeClassification.B
    elif classification == 2:
        return GradeClassification.C
    elif classification == 3:
        return GradeClassification.D
    else:
        return GradeClassification.E