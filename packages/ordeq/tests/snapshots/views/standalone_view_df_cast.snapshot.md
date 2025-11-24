## Resource

```python
import pandas as pd
from ordeq import Input, Output, node, run

dataframe = Input[pd.DataFrame](
    pd.DataFrame({
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "D": [2.0, 5.0, 8.0],
    })
)


def cast(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


df_casted = node(cast, inputs=dataframe)


class PandasHead(Output[pd.DataFrame]):
    def save(self, df: pd.DataFrame) -> None:
        print(df.head())


@node(inputs=df_casted, outputs=PandasHead())
def group_by(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(by=["A"], as_index=False, dropna=False).agg({
        "B": "mean",
        "D": "max",
    })


run(group_by, verbose=True)

```

## Output

```text
io-0 --> View:View(func=__main__:cast, ...)
View:View(func=__main__:cast, ...) --> io-1
io-1 --> Node:__main__:group_by
Node:__main__:group_by --> io-2
     A    B    D
0  bar  2.0  5.0
1  foo  2.0  8.0

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view View(func=__main__:cast, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running node 'group_by' in module '__main__'
INFO	ordeq.io	Saving Output(id=ID3)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```