from typing import Optional

from app.model.grade import Grade


class StudentPerformance:
    
    def __init__(self, age: int, gender_code: int, 
                 ethnicity_code: int, parental_education_level: int, 
                 weekly_study_time: int, absence_count: int, 
                 tutoring_status: int, parental_support_level: int, 
                 extracurricular: int, sports: int, 
                 music: int, volunteering: int, 
                 grade_classification: Grade, student_id: Optional[int] = None) -> None:
        self.age = age
        self.gender_code = gender_code
        self.ethnicity_code = ethnicity_code
        self.parental_education_level = parental_education_level
        self.weekly_study_time = weekly_study_time
        self.absence_count = absence_count
        self.tutoring_status = tutoring_status
        self.parental_support_level = parental_support_level
        self.extracurricular = extracurricular
        self.sports = sports
        self.music = music
        self.volunteering = volunteering
        self.grade_classification = grade_classification
        if student_id:
            self.student_id = student_id