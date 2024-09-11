from http import HTTPStatus
from typing import Optional
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
from pydantic import BaseModel


from app.repository.student_performance_repository import StudentPerformanceRepository
from app.schema.student_data_body import StudentDataBody
from app.schema.student_grade_prediction_response import StudentGradePredictionResponse
from app.schema.error_response import ErrorResponse
from app.model.grade import Grade
from app.schema.student_performance_by_id_path import StudentPerformanceByIdPath
from app.schema.student_performance_response import StudentPerformanceResponse, StudentPerformancesResponse
from app.schema.success_response import SuccessResponse
from app.service.grade_classification_mapper import GradeMapper
from app.service.student_performance_data_mapper import StudentPerformanceDataMapper
from app.service.student_performance_service import StudentPerformanceService

info = Info(title="MVP Predição Média Alunos API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

student_performance_tag = Tag(name='Performance do estudante', 
                              description='Lista de performance de estudantes cadastrados na base.')
prediction_tag = Tag(name='Predição da classificação da nota final do estudante ', 
                     description='Faz a predição da classificação da nota final do estudante, com base em informações demográficas' + 
                     ', hábitos de estudos, involvimento dos pais e atividades extracurriculares.')

JSON_MIMETYPE = 'application/json'

grade_mapper = GradeMapper()
data_mapper = StudentPerformanceDataMapper(grade_mapper=grade_mapper)
repository = StudentPerformanceRepository(data_mapper=data_mapper)
service = StudentPerformanceService(repository=repository, grade_mapper=grade_mapper)

@app.route('/api')
def swagger_doc():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.post(rule='/api/grade/predict', tags=[prediction_tag], 
          responses={HTTPStatus.OK: StudentGradePredictionResponse, HTTPStatus.BAD_REQUEST: ErrorResponse})
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
        print(f'Erro na predição da média: {str(e)}')
        model: BaseModel = ErrorResponse(
            error_massage=f'Erro na predição de classificação de média do estudante!'
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.BAD_REQUEST, 
            response=model.model_dump_json()
        )
    
@app.get(rule='/api/student/performances', tags=[student_performance_tag], 
         responses={HTTPStatus.OK: StudentPerformancesResponse, HTTPStatus.BAD_REQUEST: ErrorResponse})
def get_all_student_performance() -> Response:
    """Retorna todos as performances cadastradas dos estudantes com suas respectivas notas.
    """
    try:
        performances = service.get_all_performances()
        body: BaseModel = StudentPerformancesResponse(
            performances=[data_mapper.to_response(performance) for performance in performances]
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.OK, 
            response=body.model_dump_json()
        )
    except Exception as e:
        print(f'Erro na predição da média: {e}')
        body: BaseModel = ErrorResponse(
            error_massage=f'Erro na consultar performances dos estudantes!'
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.BAD_REQUEST, 
            response=body.model_dump_json()
        )
    
@app.get(rule='/api/student/performance/<int:student_id>', tags=[student_performance_tag], 
         responses={
             HTTPStatus.OK: StudentPerformanceResponse, 
             HTTPStatus.BAD_REQUEST: ErrorResponse, 
             HTTPStatus.NOT_FOUND: ErrorResponse
         })
def get_student_performance_by_id(path: StudentPerformanceByIdPath) -> Response:
    """Retorna todos as performances cadastradas dos estudantes com suas respectivas notas.
    """
    try:
        performance = service.get_student_performance_by_id(path.student_id)

        if not performance:
            print(f'Performance do estudante não encontrado para o ID')
            body: BaseModel = ErrorResponse(
                error_massage=f'Performance do estudante não encontrado para o ID {path.student_id}!'
            )
            return Response(
                mimetype=JSON_MIMETYPE,
                status=HTTPStatus.NOT_FOUND, 
                response=body.model_dump_json()
            )
        
        body = data_mapper.to_response(performance)
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.OK, 
            response=body.model_dump_json()
        )
    except Exception as e:
        print(f'Erro na consultar performances dos estudantes: {str(e)}')
        body: BaseModel = ErrorResponse(
            error_massage=f'Erro na consultar performances dos estudantes!'
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.BAD_REQUEST, 
            response=body.model_dump_json()
        )

@app.delete(rule='/api/student/performance/<int:student_id>', tags=[student_performance_tag], 
            responses={HTTPStatus.OK: SuccessResponse, HTTPStatus.BAD_REQUEST: ErrorResponse})
def remove_student_performance_by_id(path: StudentPerformanceByIdPath) -> Response:
    """Remove performance cadastrada do estudante.
    """
    try:
        service.remove_student_performance(path.student_id)

        body = SuccessResponse(
            message = "Performance do estudante excluída com sucesso!"
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.OK, 
            response=body.model_dump_json()
        )
    except Exception as e:
        print(f'Erro excluir performance do estudante: {str(e)}')
        body: BaseModel = ErrorResponse(
            error_massage=f'Erro excluir performance do estudante!'
        )
        return Response(
            mimetype=JSON_MIMETYPE,
            status=HTTPStatus.BAD_REQUEST, 
            response=body.model_dump_json()
        )