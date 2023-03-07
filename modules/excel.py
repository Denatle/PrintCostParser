import pandas as pd


def compare(val, minis, maxis):
    if val in minis:
        color = '#c2e0ff'
    elif val in maxis:
        color = '#eb3449'
    else:
        color = "white"
    return f'background-color: {color}'


class excelUtils:
    def __init__(self, indexes: list, heads: list, filename: str):
        self.indexes = indexes
        self.heads = heads
        self.file = filename

    def create_file(self, data: list[list]):
        df = pd.DataFrame(data, index=self.indexes, columns=self.heads)
        mins = []
        maxs = []
        columns = [[]for _ in range(len(df.values[0]))]
        for row in df.values:
            for i, value in enumerate(row):
                columns[i].append(value)
        for column in columns:
            mins.append(min(column))
            maxs.append(max(column))
        df.style.applymap(compare, minis=mins, maxis=maxs).to_excel(self.file)
