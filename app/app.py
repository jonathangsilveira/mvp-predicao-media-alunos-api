from http import HTTPStatus
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
from pydantic import BaseModel

from app.schema.student_data_body import StudentDataBody
from app.schema.student_grade_prediction_response import StudentGradePredictionResponse
from app.schema.error_response import ErrorResponse
from app.model.grade_classification import GradeClassification
from app.service.student_performance_service import StudentPerformanceService

info = Info(title="MVP Predição Média Alunos API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

JSON_MIMETYPE = 'application/json'

service = StudentPerformanceService()

@app.route('/api')
def swagger_doc():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.post(rule='/api/grade/predict', tags=[], 
          responses={200: StudentGradePredictionResponse, 400: ErrorResponse})
def predict_student_grade(body: StudentDataBody) -> Response:
    """Faz a predição da classificação da nota final do estudante, com base em 
    informações demográficas, hábitos de estudos, involvimento dos pais e atividades extracurriculares.
    """
    try:
        grade = service.predict(body)
        model: BaseModel = StudentGradePredictionResponse(
            grade_prediction=grade.name
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.OK, 
            response=model.model_dump_json()
        )
    except Exception as e:
        model: BaseModel = ErrorResponse(
            error_massage=f'Erro na predição de classificação de média do estudante!'
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.BAD_REQUEST, 
            response=model.model_dump_json()
        )