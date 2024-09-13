from abc import (ABC, abstractmethod)
from pandas import DataFrame
import numpy as np
import pandas

from app.schema.student_data_body import StudentDataBody


class HoldoutPreProcessor(ABC):

    @abstractmethod
    def process_holdout(self, dataset: DataFrame, test_size: float, 
                            seed: int) -> list:
        ...

class InputReshapePreProcessor(ABC):
    
    @abstractmethod
    def process_reshape(self, studentData: StudentDataBody) -> list[list]:
        ...

class InputReshapePreProcessorImpl(InputReshapePreProcessor):

    def process_reshape(self, studentData: StudentDataBody) -> list[list]:
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
            'Age', 
            'Gender', 
            'Ethnicity', 
            'ParentalEducation', 
            'StudyTimeWeekly', 
            'Absences', 
            'Tutoring', 
            'ParentalSupport', 
            'Extracurricular', 
            'Sports', 
            'Music', 
            'Volunteering'
        )
        dataframe = pandas.DataFrame(data=dataset, columns=columns)
        data: list[list] = dataframe.to_numpy()
        return data[:,0:12]