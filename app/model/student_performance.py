from typing import Optional

from app.model.grade import Grade


class StudentPerformance:
    
    def __init__(self, age: float, gender_code: float, 
                 ethnicity_code: float, parental_education_level: float, 
                 weekly_study_time: float, absence_count: float, 
                 tutoring_status: float, parental_support_level: float, 
                 extracurricular: float, sports: float, 
                 music: float, volunteering: float, 
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