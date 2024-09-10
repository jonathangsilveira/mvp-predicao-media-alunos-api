from pydantic import BaseModel

class ErrorResponse(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    error_massage: str = "Erro na predição de classificação de média do estudante!"