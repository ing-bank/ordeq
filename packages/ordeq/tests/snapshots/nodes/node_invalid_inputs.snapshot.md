## Resource

```python
from ordeq import node

print("Should raise an error:")


@node(inputs=["blabla"])
def func() -> None:
    pass

```

## Output

```text
Should raise an error:
ValueError: Input to Node(func=__main__:func, ...) must be of type Input or View, got str
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<5 lines>...
        name=f.__name__,
    )

  File "/packages/ordeq/tests/resources/nodes/node_invalid_inputs.py", line LINO, in <module>
    @node(inputs=["blabla"])
     ~~~~^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```