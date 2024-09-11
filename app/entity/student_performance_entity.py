from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from typing import Optional

BaseEntity = declarative_base()

class StudentPerformanceEntity(BaseEntity):
    __tablename__ = 'student_performance'

    student_id = Column('student_id', Integer, primary_key=True, autoincrement=True)
    age = Column('age', Integer, nullable=False)
    gender_code = Column('gender_code', Integer, nullable=False)
    ethnicity_code = Column('ethnicity_code', Integer, nullable=False)
    parental_education_level = Column('parental_education_level', Integer, nullable=False)
    weekly_study_time = Column('weekly_study_time', Integer, nullable=False)
    absence_count = Column('absences', Integer, nullable=False)
    tutoring_status = Column('tutoring', Integer, nullable=False)
    parental_support_level = Column('parental_support_level', Integer, nullable=False)
    extracurricular = Column('extracurricular', Integer, nullable=False)
    sports = Column('sports', Integer, nullable=False)
    music = Column('music', Integer, nullable=False)
    volunteering = Column('volunteering', Integer, nullable=False)
    grade_classification = Column('grade_class', Integer, nullable=False)

    def __init__(self, age: int, gender_code: int, 
                 ethnicity_code: int, parental_education_level: int, 
                 weekly_study_time: int, absence_count: int, 
                 tutoring_status: int, parental_support_level: int, 
                 extracurricular: int, sports: int, 
                 music: int, volunteering: int, 
                 grade_classification: int, student_id: Optional[int] = None) -> None:
        """
        Cria um registro de performance do estudante.

        Arguments:
            student_id: ID do estudante. Gerenciado pelo SGBD.
            age: Idade do estudante entre 15 e 18.
            gender_code: Gênero do estudante onde 0 é masculino e 1 é feminino.
            ethnicity_code: Etnia do estudante, codificado entre:
                0: Caucasiano
                1: Afrodescendente
                2: Asiático
                3: Outros
            parental_education_level: Nível de educação dos pais, codificados entre:        
                0: Nenhuma
                1: Ensino médio
                2: Ensino fundamental
                3: Ensino Superior 
                4: Acima de superior
            weekly_study_time: Frequência de estudos semanais em horas. Entre 0 e 20.
            absence_count: Número de faltas durante o ano letivo. De 0 a 30.
            tutoring_status: Indica se o estudante faz ou não aulas particulares.
            parental_support_level: Nível de suporte dos pais, indicando:        
                0: Nenhum
                1: Baixo
                2: Moderado
                3: Alto
                4: Muito alto
            extracurricular: Indica se estudante pratica atividades extracurriculares.
            sports: Indica se estudante pratica atividades esportivas.
            music: Indica se estudante pratica atividades musicais.
            volunteering: Indica se estudante pratica voluntariado.
            grade_classification: Valor de classificação entre 0 a 4.
        """
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