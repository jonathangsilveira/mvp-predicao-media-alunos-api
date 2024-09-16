from pydantic import BaseModel

class StudentPerformanceResponse(BaseModel):
    student_id: int = 1
    age: int = 15
    gender: str = 'Masculino' 
    ethnicity: str = 'Afrodescendente'
    parental_education_level: str = 'Ensino médio' 
    weekly_study_time: str = '10h'
    absence_count: int = 10
    tutoring_status: str = 'Não'
    parental_support_level: str = 'Moderado' 
    extracurricular: str = 'Não'
    sports: str = 'Sim'
    music: str = 'Sim'
    volunteering: str = 'Não'
    grade_classification: str = 'C'

class StudentPerformancesResponse(BaseModel):
    performances: list[StudentPerformanceResponse] = [
        StudentPerformanceResponse()
    ]
