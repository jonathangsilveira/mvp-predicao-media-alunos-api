from typing import Optional
import pandas as pd
import numpy as np

from app.ml_model.pipeline_delegate import PipelineDelegate
from app.model.grade import Grade
from app.model.pipeline.pipeline import PipelineLoader

from app.model.student_performance import StudentPerformance
from app.repository.student_performance_repository import StudentPerformanceRepository
from app.schema.student_data_body import StudentDataBody
from app.service.grade_classification_mapper import GradeMapper

from app.ml_model.preprocessing import InputReshapePreProcessor

PIPELINE_FILE_PATH = './machine_learning/pipelines/svm_student_performance_pipeline.pkl'

class StudentPerformanceService:

    def __init__(self, repository: StudentPerformanceRepository, 
                 grade_mapper: GradeMapper, preProcessor: InputReshapePreProcessor, 
                 pipeline: PipelineDelegate) -> None:
        self.repository = repository
        self.grade_mapper = grade_mapper
        self.preProcessor = preProcessor
        self.pipeline = pipeline

    def predict(self, studentData: StudentDataBody) -> Grade:
        input = self.preProcessor.process_reshape(studentData)

        self.pipeline.load(PIPELINE_FILE_PATH)
        
        prediction = self.pipeline.predict(input)
        outcome = int(prediction[0])
        grade = self.grade_mapper.map(outcome)

        self.__insert_student_performance__(studentData, grade)

        return grade
    
    def get_all_performances(self) -> list[StudentPerformance]:
        return self.repository.all()

    def get_student_performance_by_id(self, student_id: int) -> Optional[StudentPerformance]:
        return self.repository.get(student_id=student_id)
    
    def remove_student_performance(self, student_id: int) -> None:
        self.repository.remove(student_id=student_id)
        
    def __insert_student_performance__(self, studentData: StudentDataBody, grade: Grade) -> None:
        performance = StudentPerformance(
            age=studentData.age, 
            gender_code=studentData.gender_code, 
            ethnicity_code=studentData.ethnicity_code,
            parental_education_level=studentData.parental_education_level,
            weekly_study_time=studentData.weekly_study_time,
            absence_count=studentData.absence_count,
            tutoring_status=studentData.tutoring_status,
            parental_support_level=studentData.parental_support_level,
            extracurricular=studentData.extracurricular,
            sports=studentData.sports,
            music=studentData.music,
            volunteering=studentData.volunteering,
            grade_classification=grade
        )
        self.repository.insert(performance)
