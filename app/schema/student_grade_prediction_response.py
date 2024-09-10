from pydantic import BaseModel

class StudentGradePredictionResponse(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    grade_prediction: str = "A"