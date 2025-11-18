## Resource

```python
# Captures the behaviour when a node is created with a non-supported argument.
from ordeq import node


@node(None)
def my_node() -> None:
    print("Hello, world!")

```

## Output

```text
ValueError: The first argument to node must be a function, got NoneType
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/nodes/node_none.py", line LINO, in <module>
    @node(None)
     ~~~~^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```