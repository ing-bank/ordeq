## Resource

```python
import pandas as pd
from ordeq import Output, node, run
from ordeq_common import Literal

dataframe = Literal(
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
View:standalone_view_df_cast:cast --> io-1
io-1 --> Node:standalone_view_df_cast:group_by
Node:standalone_view_df_cast:group_by --> io-2
     A    B    D
0  bar  2.0  5.0
1  foo  2.0  8.0

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_cast:cast'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.runner	Running view "cast" in module "standalone_view_df_cast"
INFO	ordeq.runner	Running node "group_by" in module "standalone_view_df_cast"
INFO	ordeq.io	Saving Output(idx=ID1)

```