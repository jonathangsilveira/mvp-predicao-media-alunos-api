from typing import Optional
from app.entity.student_performance_entity import StudentPerformanceEntity
from app.database import Session
from app.model.student_performance import StudentPerformance
from app.schema.student_performance_response import StudentPerformanceResponse
from app.service.student_performance_data_mapper import StudentPerformanceDataMapper


class StudentPerformanceRepository:

    def __init__(self, data_mapper: StudentPerformanceDataMapper) -> None:
        self.data_mapper = data_mapper

    def insert(self, performance: StudentPerformance) -> None:
        """
        Insere uma nova performance de estudante com sua classificação predita.

        Arguments:
            performance: Registro de performance da entidade.

        """
        entity = self.data_mapper.to_entity(performance)
        with Session() as session:
            with session.begin():
                session.add(entity)
                session.commit()

    def get(self, student_id: int) -> Optional[StudentPerformanceResponse]:
        """
        Retorna um registro de performance do estudante pelo ID.

        Arguments:
            student_id: Identificador único de performance do estudante.

        Return:
            registro de performance do estudante pelo ID ou None caso não encontrar.
        """
        with Session() as session:
            performance = session.get(StudentPerformanceEntity, student_id)
            return self.data_mapper.to_model(performance) if performance else None

    def all(self) -> list[StudentPerformance]:
        """
        Retorna todos os registros de performance armazenados.

        Return:
            Todos os registros de performance do estudante ou uma lista vazia caso não houver.
        """
        with Session() as session:
            performances = session.query(StudentPerformanceEntity).all()
            return [self.data_mapper.to_model(performance) for performance in performances]
        
    def remove(self, student_id: int) -> None:
        """
        Remove o registro de performance armazenado pelo ID caso existir.
        """
        with Session() as session:
            with session.begin():
                performance = session.get(StudentPerformanceEntity, student_id)
                if performance:
                    session.delete(performance)
                    session.commit()