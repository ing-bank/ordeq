## Resource

```python
import pandas as pd
from ordeq import node, run
from ordeq_common import Literal

dataframe = Literal(
    pd.DataFrame({
        "A": ["foo", "bar", "foo"],
        "B": [1, 2, 3],
        "C": ["one", "one", "two"],
        "gt": [2.0, 5.0, 8.0],
    })
)

Split = tuple[pd.DataFrame, pd.DataFrame]


@node(inputs=dataframe)
def split(df: pd.DataFrame) -> Split:
    df = df.sample(frac=1, random_state=1).reset_index(drop=True)
    n_test = int(len(df) * 0.25)
    test_df = df.iloc[:n_test]
    train_df = df.iloc[n_test:]
    return train_df, test_df


@node(inputs=split)
def train(data: Split) -> None:
    # Put your training code here
    print("Training", data[0].describe())


run(train, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_train_test_split.py", line LINO, in <module>
    run(train, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^

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
     view_train_test_split:split -> [view_train_test_split:train]
     view_train_test_split:train -> []
  Nodes:
     view_train_test_split:split: View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])
     view_train_test_split:train: View(name=view_train_test_split:train, inputs=[View(name=view_train_test_split:split, inputs=[Literal(     A  B    C   gt
0  foo  1  one  2.0
1  bar  2  one  5.0
2  foo  3  two  8.0)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_train_test_split:split'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_train_test_split:train'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```