## Resource

```python
from ordeq import node, run
from ordeq_common import Literal
import pandas as pd


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


print(run(aggregate, verbose=True))

```

## Exception

```text
IOException: Failed to load IO(idx=ID1).

```

## Output

```text
NodeGraph:
  Edges:
     view_to_pandas:aggregate -> [view_to_pandas:csv_as_df]
     view_to_pandas:csv_as_df -> []
  Nodes:
     View(name=view_to_pandas:aggregate, inputs=[View(name=view_to_pandas:csv_as_df, inputs=[Literal(<view_to_pandas.MockDuckDbValues object at HASH1>)])])
     View(name=view_to_pandas:csv_as_df, inputs=[Literal(<view_to_pandas.MockDuckDbValues object at HASH1>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_to_pandas:csv_as_df'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_to_pandas:aggregate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading IO(idx=ID1)

```