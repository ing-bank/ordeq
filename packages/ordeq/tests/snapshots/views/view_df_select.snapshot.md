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
def df_selected(df: pd.DataFrame) -> pd.DataFrame:
    return df["A"].to_frame()


@node(inputs=df_selected)
def group_by(df: pd.DataFrame) -> None:
    print(df.groupby(
        by=["A"],
        as_index=False,
        dropna=False,
    ).agg("mean").head())


run(group_by, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     view_df_select:df_selected -> [view_df_select:group_by]
     view_df_select:group_by -> []
  Nodes:
     view_df_select:df_selected: View(name=view_df_select:df_selected, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
     view_df_select:group_by: View(name=view_df_select:group_by, inputs=[View(name=view_df_select:df_selected, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])
     A
0  bar
1  foo

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_select:df_selected'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_select:group_by'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)
INFO	ordeq.runner	Running view "df_selected" in module "view_df_select"
INFO	ordeq.runner	Running view "group_by" in module "view_df_select"

```