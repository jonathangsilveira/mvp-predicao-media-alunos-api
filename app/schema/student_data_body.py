from pydantic import BaseModel

class StudentDataBody(BaseModel):
    age: int = 15
    gender_code: int = 1 
    ethnicity_code: int = 1
    parental_education_level: int = 1 
    weekly_study_time: int = 10
    absence_count: int = 10
    tutoring_status: int = 0
    parental_support_level: int = 3 
    extracurricular: int = 0
    sports: int = 1
    music: int = 0
    volunteering: int = 0
