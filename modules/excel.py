import pandas as pd


class excelWriter:
    def __init__(self, indexes: list, heads: list, filename: str):
        self.indexes = indexes
        self.heads = heads
        self.file = filename

    def write(self, data: list[list]):
        df = pd.DataFrame(data, index=self.indexes, columns=self.heads)
        df.to_excel(self.file)
