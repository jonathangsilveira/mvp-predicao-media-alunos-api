from pandas import DataFrame

from app.model.preprocessing.cleanup_strategies import CleanupStrategy
from app.model.preprocessing.holdout_strategies import HoldoutStrategy

class PreProcessor:

    def __init__(self, holdoutStrategy: HoldoutStrategy, cleanupStrategy: CleanupStrategy) -> None:
        self.holdoutStrategy = holdoutStrategy
        self.cleanupStrategy = cleanupStrategy

    def pre_process(self, dataframe: DataFrame, 
                    test_size: float, seed: int) -> list:
        self.cleanupStrategy.cleanup(dataframe)

        x_train, x_test, y_train, y_test = self.holdoutStrategy.split(
            dataframe=dataframe, 
            test_size=test_size, 
            seed=seed
        )
        return (x_train, x_test, y_train, y_test)