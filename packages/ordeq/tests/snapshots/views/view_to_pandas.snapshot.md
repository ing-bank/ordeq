## Resource

```python
import pandas as pd
from ordeq import Input, node, run


class MockDuckDbValues:
    def __init__(self, data):
        self.data = data

    def to_df(self):
        return pd.DataFrame(self.data, columns=["value"])


csv = Input(MockDuckDbValues((1, 2, 3)))


@node(inputs=csv)
def csv_as_df(data: MockDuckDbValues) -> pd.DataFrame:
    return data.to_df()


@node(inputs=csv_as_df)
def aggregate(df: pd.DataFrame) -> None:
    print(df.aggregate("sum").head())


run(aggregate, verbose=True)

```

## Output

```text
io-0 --> View:__main__:csv_as_df
View:__main__:csv_as_df --> io-1
io-1 --> View:__main__:aggregate
View:__main__:aggregate --> io-2
value    6
dtype: int64

```

## Logging

```text
INFO	ordeq.runner	Running view 'csv_as_df' in module '__main__'
INFO	ordeq.runner	Running view 'aggregate' in module '__main__'

```