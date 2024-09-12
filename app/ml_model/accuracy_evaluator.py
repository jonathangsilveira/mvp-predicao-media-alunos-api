from sklearn.metrics import accuracy_score

from app.ml_model.pipeline_delegate import PipelineDelegate


class AccuracyEvaluator:
    """
    Implementação para avaliar acurácia de um modelo pré-treinado.
    """

    def evaluate(self, pipeline: PipelineDelegate, 
                 x_test: list[list], y_test: list) -> float:
        predictions = pipeline.predict(x_test)
        return accuracy_score(y_test, predictions)