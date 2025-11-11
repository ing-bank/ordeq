## Resource

```python
from ordeq import IO, node


@node(input=IO(), outputs=IO())
def my_node(a):
    return a

```

## Exception

```text
ValueError: The 'input' keyword argument is not supported. Did you mean 'inputs'?
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/nodes/node_input.py", line LINO, in <module>
    @node(input=IO(), outputs=IO())
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```