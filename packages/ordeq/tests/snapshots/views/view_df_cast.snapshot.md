## Resource

```python
from ordeq import node, run
import pandas as pd
from ordeq_common import Literal

dataframe = Literal(
    pd.DataFrame(
        {
            "A": ["foo", "bar", "foo"],
            "B": [1, 2, 3],
            "C": ["one", "one", "two"],
            "D": [2.0, 5.0, 8.0],
        }
    )
)


@node(inputs=dataframe)
def df_casted(df: pd.DataFrame) -> pd.DataFrame:
    df["A"] = df["A"].astype("string")
    return df


@node(inputs=df_casted)
def group_by(df: pd.DataFrame) -> None:
    print(df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg({"B": "mean", "D": "max"}).head())


print(run(group_by, verbose=True))

```

## Output

```text
NodeGraph:
  Edges:
     view_df_cast:df_casted -> [view_df_cast:group_by]
     view_df_cast:group_by -> []
  Nodes:
     View(name=view_df_cast:df_casted, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
     View(name=view_df_cast:group_by, inputs=[View(name=view_df_cast:df_casted, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])
     A    B    D
0  bar  2.0  5.0
1  foo  2.0  8.0
{View(name=view_df_cast:df_casted, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)]):      A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0, View(name=view_df_cast:group_by, inputs=[View(name=view_df_cast:df_casted, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])]): None}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_cast:df_casted'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_cast:group_by'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.runner	Running node View(name=view_df_cast:df_casted, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
INFO	ordeq.runner	Running node View(name=view_df_cast:group_by, inputs=[IO(idx=ID1)])

```