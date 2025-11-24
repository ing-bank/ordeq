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
INFO	ordeq.runner	Running view View(func=__main__:filter_df, ...)
INFO	ordeq.runner	Running view 'group_by' in module '__main__'

```