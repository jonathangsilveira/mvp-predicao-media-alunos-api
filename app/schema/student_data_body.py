from pydantic import BaseModel

class StudentDataBody(BaseModel):
    age: float = 15.0
    gender_code: float = 1.0 
    ethnicity_code: float = 1.0
    parental_education_level: float = 1.0 
    weekly_study_time: float = 10.0
    absence_count: float = 10.0
    tutoring_status: float = 0.0
    parental_support_level: float = 3.0 
    extracurricular: float = 0.0
    sports: float = 1.0
    music: float = 0.0
    volunteering: float = 0.0
