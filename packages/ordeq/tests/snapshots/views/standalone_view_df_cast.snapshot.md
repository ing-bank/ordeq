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

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/standalone_view_df_cast.py", line LINO, in <module>
    run(group_by, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     standalone_view_df_cast:cast -> [standalone_view_df_cast:group_by]
     standalone_view_df_cast:group_by -> []
  Nodes:
     standalone_view_df_cast:cast: View(name=standalone_view_df_cast:cast, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
     standalone_view_df_cast:group_by: Node(name=standalone_view_df_cast:group_by, inputs=[View(name=standalone_view_df_cast:cast, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])], outputs=[Output(idx=ID1)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_cast:cast'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```