## Resource

```python
from ordeq import node
from ordeq_common import Literal


@node(inputs=[Literal("a"), Literal("b")])
def my_node(*, a, b):
    print(f"a: {a}, b: {b}")

```

## Output

```text
ValueError: Inputs invalid for function arguments: '__main__:my_node'
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_for_invalid_inputs
    raise ValueError(
        f"Inputs invalid for function arguments: '{n}'"
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_for_invalid_inputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line LINO, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    return View(
        func=func,  # type: ignore[arg-type]
    ...<6 lines>...
        name=name,  # type: ignore[arg-type]
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<5 lines>...
        name=f.__name__,
    )

  File "/packages/ordeq/tests/resources/nodes/node_kwarg_only.py", line LINO, in <module>
    @node(inputs=[Literal("a"), Literal("b")])
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```