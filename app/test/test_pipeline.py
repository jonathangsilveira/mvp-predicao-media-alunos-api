
from app.ml_model.cvs_dataset_loader import CSVDatasetLoader
from app.ml_model.accuracy_evaluator import AccuracyEvaluator
from app.ml_model.pipeline_wrapper import PipelineWrapper

dataset_loader = CSVDatasetLoader()
evaluator = AccuracyEvaluator()
pipeline = PipelineWrapper()

x_dataset_filepath = './machine_learning/data/x_test_dataset_student_performance.csv'
y_dataset_filepath = './machine_learning/data/y_test_dataset_student_performance.csv'
x_dataframe = dataset_loader.load(source=x_dataset_filepath)
y_dataframe = dataset_loader.load(source=y_dataset_filepath)

x_data = x_dataframe.to_numpy()
y_data = y_dataframe.to_numpy()
x = x_data[:,0:12]
y = y_data[:,-1]

def test_pipeline_svm_model() -> None:
    # Given
    pipeline_filepath = './machine_learning/pipelines/svm_student_performance_pipeline.pkl'
    pipeline.load(pipeline_filepath)

    # When
    accuracy_pipeline = evaluator.evaluate(pipeline=pipeline, x_test=x, y_test=y)

    # Then
    assert 0.71 <= accuracy_pipeline <= 0.76
    