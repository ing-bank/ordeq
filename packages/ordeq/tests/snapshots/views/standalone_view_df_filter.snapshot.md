## Resource

```python
import pandas as pd
from ordeq import Output, node, run
from ordeq_common import Literal

df = pd.DataFrame({
    "A": ["foo", "bar", "foo"],
    "B": [1, 2, 3],
    "C": ["one", "one", "two"],
    "D": [2.0, 5.0, 8.0],
})

dataframe = Literal(df)

fltr = Literal(df["B"] > 4)


def filter_df(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    return df.where(condition)


df_filtered = node(filter_df, inputs=[dataframe, fltr])


class PandasHead(Output[pd.DataFrame]):
    def save(self, df: pd.DataFrame) -> None:
        print(df.head())


@node(inputs=df_filtered)
def group_by(df: pd.DataFrame) -> None:
    print(
        df.groupby(by=["A"], as_index=False, dropna=False)
        .agg({"B": "mean", "D": "max"})
        .head()
    )


run(group_by, verbose=True)

```

## Output

```text
io-0 --> View:View(func=__main__:filter_df, ...)
io-1 --> View:View(func=__main__:filter_df, ...)
View:View(func=__main__:filter_df, ...) --> io-2
io-2 --> View:__main__:group_by
View:__main__:group_by --> io-3
     A   B   D
0  NaN NaN NaN

```

## Logging

```text
INFO	ordeq.io	Loading Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
DEBUG	ordeq.io	Persisting data for Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.io	Loading Literal(0    False
1    False
2    False
Name: B, dtype: bool)
DEBUG	ordeq.io	Persisting data for Literal(0    False
1    False
2    False
Name: B, dtype: bool)
INFO	ordeq.runner	Running view View(func=__main__:filter_df, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'group_by' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
DEBUG	ordeq.io	Unpersisting data for Literal(0    False
1    False
2    False
Name: B, dtype: bool)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```