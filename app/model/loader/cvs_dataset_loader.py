from pandas import (DataFrame, read_csv)

from dataset_loader import DatasetLoader

class CVSDatasetLoader(DatasetLoader):

    def load(self, source: any, attributes: list[str]) -> DataFrame:
        return read_csv(str(source), skiprows=0, delimiter=',')