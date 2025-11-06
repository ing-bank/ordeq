## Resource

```python
# Captures the behaviour when a node is created with a non-supported argument.
from ordeq import node


@node(None)
def my_node() -> None:
    print("Hello, world!")

```

## Exception

```text
ValueError: The first argument to node must be a function, got NoneType
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/nodes/node_none.py", line LINO, in <module>
    @node(None)
     ~~~~^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```