from pydantic import BaseModel

class SuccessResponse(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    massage: str = "Performance do estudante excluída com sucesso!"