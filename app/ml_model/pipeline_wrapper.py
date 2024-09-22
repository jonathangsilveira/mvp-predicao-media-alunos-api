
from typing import Optional
from sklearn.pipeline import Pipeline
import numpy as np
import pickle

class PipelineWrapper:
    pipeline: Optional[Pipeline] = None

    def load(self, filepath: str) -> None:
        """Carregamos o pipeline construindo durante a fase de treinamento através do arquivo.
        """
        
        with open(filepath, 'rb') as file:
             self.pipeline = pickle.load(file)

    def predict(self, x_input: list[list]) -> list[float]:
        """Realiza a predição de média do estudante com base no modelo treinado.
        """

        return self.pipeline.predict(x_input) if self.pipeline else []
