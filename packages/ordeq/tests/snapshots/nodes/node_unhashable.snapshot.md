## Resource

```python
from dataclasses import dataclass

from ordeq import Input, node
from ordeq_common import StringBuffer


@dataclass(frozen=True)
class Unhashable(Input[list]):
    # This input is unhashable because its data attribute is a list.
    data: list

    def load(self) -> list:
        return self.data


@node(inputs=[Unhashable(["y", "z"])], outputs=StringBuffer("y"))
def func(x: str) -> str:
    return x

```

## Output

```text
ValueError: Node is not hashable: Node(name=__main__:func, inputs=[Unhashable(data=['y', 'z'])], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_if_not_hashable
    raise ValueError(f"Node is not hashable: {n}") from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_if_not_hashable(self)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^

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
    inner.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        inner, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/nodes/node_unhashable.py", line LINO, in <module>
    @node(inputs=[Unhashable(["y", "z"])], outputs=StringBuffer("y"))
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```