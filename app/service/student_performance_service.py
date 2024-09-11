from typing import Optional
import pandas as pd
import numpy as np

from app.model.grade import Grade
from app.model.pipeline.pipeline import PipelineLoader

from app.model.student_performance import StudentPerformance
from app.repository.student_performance_repository import StudentPerformanceRepository
from app.schema.student_data_body import StudentDataBody
from app.schema.student_grade_prediction_response import StudentGradePredictionResponse
from app.service.grade_classification_mapper import GradeMapper

PIPELINE_FILE_PATH = './machine_learning/pipelines/svm_student_performance_pipeline.pkl'

class StudentPerformanceService:

    def __init__(self, repository: StudentPerformanceRepository, 
                 grade_mapper: GradeMapper) -> None:
        self.repository = repository
        self.grade_mapper = grade_mapper

    def predict(self, studentData: StudentDataBody) -> Grade:
        input = self.__pre_process__(studentData)

        loader = PipelineLoader()
        pipeline = loader.load_pipeline(filepath=PIPELINE_FILE_PATH)
        
        prediction = pipeline.predict(input)
        outcome = int(prediction[0])

        self.__insert_student_performance__(studentData, outcome)

        return self.grade_mapper.map(classification=outcome)
    
    def get_all_performances(self) -> list[StudentPerformance]:
        return self.repository.all()

    def get_student_performance_by_id(self, student_id: int) -> Optional[StudentPerformance]:
        return self.repository.get(student_id=student_id)
    
    def remove_student_performance(self, student_id: int) -> None:
        self.repository.remove(student_id=student_id)
        
    def __pre_process__(self, studentData: StudentDataBody) -> list[list]:
        x_input = np.array([
            studentData.age, 
            studentData.gender_code, 
            studentData.ethnicity_code,
            studentData.parental_education_level,
            studentData.weekly_study_time,
            studentData.absence_count,
            studentData.tutoring_status,
            studentData.parental_support_level,
            studentData.extracurricular,
            studentData.sports,
            studentData.music,
            studentData.volunteering
        ])
        dataset: list[list] = x_input.reshape(1, -1)
        columns = (
            'age',
            'gender_code',
            'ethnicity_code',
            'parental_education_level',
            'weekly_study_time',
            'absence_count',
            'tutoring_status',
            'parental_support_level',
            'extracurricular',
            'sports',
            'music',
            'volunteering'
        )
        dataframe = pd.DataFrame(data=dataset, columns=columns)
        data: list[list] = dataframe.to_numpy()
        return data[:,0:11]
    
    def __insert_student_performance__(self, studentData: StudentDataBody, prediction: int) -> None:
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
            grade_classification=self.grade_mapper.map(prediction)
        )
        self.repository.insert(performance)
