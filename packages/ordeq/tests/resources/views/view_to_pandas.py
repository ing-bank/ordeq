import pandas as pd
from ordeq import Input, node, run


class MockDuckDbValues:
    def __init__(self, data):
        self.data = data

    def to_df(self):
        return pd.DataFrame(self.data, columns=["value"])


csv = Input[MockDuckDbValues](MockDuckDbValues((1, 2, 3)))


@node(inputs=csv)
def csv_as_df(data: MockDuckDbValues) -> pd.DataFrame:
    return data.to_df()


@node(inputs=csv_as_df)
def aggregate(df: pd.DataFrame) -> None:
    print(df.aggregate("sum").head())


run(aggregate, verbose=True)
