
from abc import (ABC, abstractmethod)
from pandas import DataFrame


class CleanupStrategy(ABC):

    @abstractmethod
    def cleanup(self, dataframe: DataFrame) -> None:
        ...

class UnnecessaryColumnsCleanupStrategy(CleanupStrategy):

    def cleanup(self, dataframe: DataFrame) -> None:
        dataframe.drop(['StudentID', 'GPA'], axis=1, inplace=True)