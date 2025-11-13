## Resource

```python
import pandas as pd
from ordeq import node, run
from ordeq_common import Literal


class MockDuckDbValues:
    def __init__(self, data):
        self.data = data

    def to_df(self):
        return pd.DataFrame(self.data, columns=["value"])


csv = Literal(MockDuckDbValues((1, 2, 3)))


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
io-2 --> View:__main__:csv_as_df
View:__main__:csv_as_df --> io-0
io-0 --> View:__main__:aggregate
View:__main__:aggregate --> io-1
value    6
dtype: int64

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:csv_as_df'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:aggregate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<__main__.MockDuckDbValues object at HASH1>)
INFO	ordeq.runner	Running view "csv_as_df" in module "__main__"
INFO	ordeq.runner	Running view "aggregate" in module "__main__"

```