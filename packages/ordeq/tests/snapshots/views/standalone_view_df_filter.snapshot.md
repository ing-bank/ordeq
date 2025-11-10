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
io-0 --> View:standalone_view_df_filter:group_by
io-2 --> View:standalone_view_df_filter:filter_df
io-3 --> View:standalone_view_df_filter:filter_df
View:standalone_view_df_filter:group_by --> io-1
View:standalone_view_df_filter:filter_df --> io-0
     A   B   D
0  NaN NaN NaN

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_filter:filter_df'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_filter:group_by'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.io	Loading Literal(0    False
1    False
2    False
Name: B, dtype: bool)
INFO	ordeq.runner	Running view "filter_df" in module "standalone_view_df_filter"
INFO	ordeq.runner	Running view "group_by" in module "standalone_view_df_filter"

```