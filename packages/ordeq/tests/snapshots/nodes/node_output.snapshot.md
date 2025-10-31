## Resource

```python
from ordeq import IO, node


@node(inputs=IO(), output=IO())
def my_node(a):
    return a

```

## Exception

```text
ValueError: The 'output' keyword argument is not supported. Did you mean 'outputs'?
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/nodes/node_output.py", line LINO, in <module>
    @node(inputs=IO(), output=IO())
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```