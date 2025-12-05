## Resource

```python
import pandas as pd
from ordeq import Input, Output, node, run

df = pd.DataFrame({
    "A": ["foo", "bar", "foo"],
    "B": [1, 2, 3],
    "C": ["one", "one", "two"],
    "D": [2.0, 5.0, 8.0],
})

dataframe = Input(df)

fltr = Input(df["B"] > 4)


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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
INFO	ordeq.runner	Loading Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
INFO	ordeq.runner	Loading Input(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID2)
INFO	ordeq.runner	Running View(func=__main__:filter_df, ...)
INFO	ordeq.runner	Saving IO 'group_by:df' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'group_by:df' in module '__main__'
INFO	ordeq.runner	Loading IO 'group_by:df' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'group_by:df' in module '__main__'
INFO	ordeq.runner	Running view 'group_by' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO 'group_by:df' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```