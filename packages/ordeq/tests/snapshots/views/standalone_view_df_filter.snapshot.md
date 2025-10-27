## Resource

```python
from ordeq import node, run
import pandas as pd
from ordeq import Output
from ordeq_common import Literal

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "D": [2.0, 5.0, 8.0],
    }
)

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
    print(df.groupby(
        by=["A", ],
        as_index=False,
        dropna=False,
    ).agg(
        {"B": "mean", "D": "max"}
    ).head())


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

  File "/packages/ordeq/tests/resources/views/standalone_view_df_filter.py", line 43, in <module>
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
     standalone_view_df_filter:group_by -> []
  Nodes:
     standalone_view_df_filter:group_by: View(name=standalone_view_df_filter:group_by, inputs=[View(name=standalone_view_df_filter:filter_df, inputs=[Literal(     A  B    C    D
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0), Literal(0    False
1    False
2    False
Name: B, dtype: bool)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_filter:filter_df'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'standalone_view_df_filter:group_by'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:21: error: No overload variant of "where" of "DataFrame" matches argument type "str"  [call-overload]
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:21: note: Possible overload variants:
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:21: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[True], axis: Literal['index', 0] | Literal['columns', 1] | None = ..., level: Hashable | None = ...) -> None
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:21: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[False] = ..., axis: Literal['index', 0, 'columns', 1] | None = ..., level: Hashable | None = ...) -> DataFrame
Found 1 error in 1 file (checked 1 source file)

```