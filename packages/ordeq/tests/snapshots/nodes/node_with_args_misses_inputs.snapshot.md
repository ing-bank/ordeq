## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=[StringBuffer("a")])
def func(a: str) -> str:
    return a


run(func)

```

## Output

```text
ValueError: Node inputs invalid for function arguments: Node(func=__main__:func, ...)
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_for_invalid_inputs
    raise ValueError(
        f"Node inputs invalid for function arguments: {n}"
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_for_invalid_inputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line LINO, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    return Node(
        func=func,
    ...<4 lines>...
        views=tuple(views),
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<3 lines>...
        attributes=attributes,
    )

  File "/packages/ordeq/tests/resources/nodes/node_with_args_misses_inputs.py", line LINO, in <module>
    @node(outputs=[StringBuffer("a")])
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```