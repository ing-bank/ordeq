## Resource

```python
from ordeq import node, run
import pandas as pd
from ordeq_common import Literal

dataframe= Literal(
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


print(run(group_by, verbose=True))

```

## Exception

```text
AttributeError: 'View' object has no attribute 'load'
  File "/packages/ordeq/src/ordeq/_runner.py", line 55, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 134, in _run_graph
    computed = _run_node(
        name, patched_nodes[name, node], hooks=hooks, save=save_node
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line 186, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/views/view_df_select.py", line 31, in <module>
    print(run(group_by, verbose=True))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     view_df_select:group_by -> []
  Nodes:
     view_df_select:group_by: View(name=view_df_select:group_by, inputs=[View(name=view_df_select:df_selected, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_select:df_selected'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_df_select:group_by'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```