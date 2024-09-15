
from app.entity.student_performance_entity import StudentPerformanceEntity
from app.model.grade import Grade
from app.model.student_performance import StudentPerformance
from app.schema.student_performance_response import StudentPerformanceResponse
from app.service.grade_classification_mapper import GradeMapper


class StudentPerformanceDataMapper:

    def __init__(self, grade_mapper: GradeMapper) -> None:
        self.grade_mapper = grade_mapper

    def to_response(self, model: StudentPerformance) -> StudentPerformanceResponse:
        return StudentPerformanceResponse(
            student_id=model.student_id,
            age=model.age, 
            gender_code=model.gender_code, 
            ethnicity_code=model.ethnicity_code,
            parental_education_level=model.parental_education_level,
            weekly_study_time=model.weekly_study_time,
            absence_count=model.absence_count,
            tutoring_status=model.tutoring_status,
            parental_support_level=model.parental_support_level,
            extracurricular=model.extracurricular,
            sports=model.sports,
            music=model.music,
            volunteering=model.volunteering,
            grade_classification=model.grade_classification.name
        )

    def to_model(self, entity: StudentPerformanceEntity) -> StudentPerformance:
        return StudentPerformance(
            student_id=entity.student_id,
            age=entity.age, 
            gender_code=entity.gender_code, 
            ethnicity_code=entity.ethnicity_code,
            parental_education_level=entity.parental_education_level,
            weekly_study_time=entity.weekly_study_time,
            absence_count=entity.absence_count,
            tutoring_status=entity.tutoring_status,
            parental_support_level=entity.parental_support_level,
            extracurricular=entity.extracurricular,
            sports=entity.sports,
            music=entity.music,
            volunteering=entity.volunteering,
            grade_classification=self.grade_mapper.map(entity.grade_classification)
        )

    def to_entity(self, performance: StudentPerformance) -> StudentPerformanceEntity:
        return StudentPerformanceEntity(
            age=performance.age, 
            gender_code=performance.gender_code, 
            ethnicity_code=performance.ethnicity_code,
            parental_education_level=performance.parental_education_level,
            weekly_study_time=performance.weekly_study_time,
            absence_count=performance.absence_count,
            tutoring_status=performance.tutoring_status,
            parental_support_level=performance.parental_support_level,
            extracurricular=performance.extracurricular,
            sports=performance.sports,
            music=performance.music,
            volunteering=performance.volunteering,
            grade_classification=performance.grade_classification.value
        )
    
    def __translate_educational_level(self, value: float) -> str:
        if value < 1.0:
            return 'Nenhuma'
        elif value < 2.0:
            return 'Ensino médio'
        elif value < 3.0:
            return 'Ensino fundamental'
        elif value < 4.0:
            return 'Ensino Superior'
        else:
            return 'Acima de superior'
        
    def __translate_support_level(self, value: float) -> str:
        if value < 1.0:
            return 'Nenhum'
        elif value < 2.0:
            return 'Baixo'
        elif value < 3.0:
            return 'Moderado'
        elif value < 4.0:
            return 'Alto'
        else:
            return 'Muito alto'
        
    def __translate_gender(self, value: float) -> str:
        if value <= 1.0:
            return 'Masculino'
        else:
            return 'Feminino'
        
    def __translate_ethnicity(self, value: float) -> str:
        if value < 1.0:
            return 'Caucasiano'
        elif value < 2.0:
            return 'Afrodescendente'
        elif value < 3.0:
            return 'Asiático'
        else:
            return 'Outros'
        
    def __to_bool(self, value: float) -> bool:
        if value < 1.0:
            return False
        else:
            return True