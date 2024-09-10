import pandas as pd
import numpy as np

from app.entity.student_performance import StudentPerformanceEntity
from app.model.grade_classification import GradeClassification
from app.model.pipeline.pipeline import PipelineLoader

from app.schema.student_data_body import StudentDataBody
from app.database import Session
from app.service.grade_classification_mapper import to_grade_classification

PIPELINE_FILE_PATH = './machine_learning/pipelines/svm_student_performance_pipeline.pkl'

class StudentPerformanceService:

    def predict(self, studentData: StudentDataBody) -> GradeClassification:
        input = self.__pre_process__(studentData)

        loader = PipelineLoader()
        pipeline = loader.load_pipeline(filepath=PIPELINE_FILE_PATH)
        
        prediction = pipeline.predict(input)
        outcome = int(prediction[0])

        self.__add_student_performance__(studentData, outcome)

        return to_grade_classification(classification=outcome)
        
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
    
    def __add_student_performance__(self, studentData: StudentDataBody, prediction: int) -> None:
        session = Session()
        try:
            entity = StudentPerformanceEntity(
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
                grade_classification=prediction
            )
            session.add(entity)
            session.commit()
        except Exception as e:
            raise e
        finally:
            session.close()
