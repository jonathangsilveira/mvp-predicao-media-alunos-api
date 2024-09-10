from abc import ABC, abstractmethod
from pandas import DataFrame

class DatasetLoader(ABC):

    @abstractmethod
    def load(self, source: any, attributes: list[str]) -> DataFrame:
        ...