import pickle
from sklearn.pipeline import Pipeline

class PipelineLoader:

    def load_pipeline(self, filepath: str) -> Pipeline:
        """Carregamos o pipeline construindo durante a fase de treinamento
        """
        
        with open(filepath, 'rb') as file:
             pipeline = pickle.load(file)
        return pipeline