from abc import ABC, abstractmethod
from pandas import DataFrame
from sklearn.model_selection import train_test_split

class HoldoutStrategy(ABC):

    @abstractmethod
    def split(self, dataframe: DataFrame, test_size: float, 
              seed: int) -> list[list]:
        ...

class StudentPerformanceHoldoutStrategy(HoldoutStrategy):

    def split(self, dataframe: DataFrame, test_size: 
              float, seed: int) -> list[list]:
        
        data: list[list] = dataframe.to_numpy()
        x: list[list] = data[:,0:11] # From first column index to the last one
        y: list = data[:,-1] # It gets each cell from the last column index.
        return train_test_split(x, y, test_size=test_size, random_state=seed)