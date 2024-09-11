

from pydantic import BaseModel


class StudentPerformanceByIdPath(BaseModel):
    student_id: int = 1