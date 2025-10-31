## Resource

```python
import pandas as pd
from ordeq import node, run
from ordeq_common import Literal


class MockDuckDbValues:
    def __init__(self, data):
        self.data = data

    def to_df(self):
        return pd.DataFrame(self.data, columns=["value"])


csv = Literal(MockDuckDbValues((1, 2, 3)))


@node(inputs=csv)
def csv_as_df(data: MockDuckDbValues) -> pd.DataFrame:
    return data.to_df()


@node(inputs=csv_as_df)
def aggregate(df: pd.DataFrame) -> None:
    print(df.aggregate("sum").head())


run(aggregate, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_to_pandas.py", line LINO, in <module>
    run(aggregate, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^

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
     view_to_pandas:aggregate -> []
     view_to_pandas:csv_as_df -> [view_to_pandas:aggregate]
  Nodes:
     view_to_pandas:aggregate: View(name=view_to_pandas:aggregate, inputs=[View(name=view_to_pandas:csv_as_df, inputs=[Literal(<view_to_pandas.MockDuckDbValues object at HASH1>)])])
     view_to_pandas:csv_as_df: View(name=view_to_pandas:csv_as_df, inputs=[Literal(<view_to_pandas.MockDuckDbValues object at HASH1>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_to_pandas:csv_as_df'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_to_pandas:aggregate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```