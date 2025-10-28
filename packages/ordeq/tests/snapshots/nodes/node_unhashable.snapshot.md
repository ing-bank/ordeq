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

## Exception

```text
ValueError: Node is not hashable: Node(name=node_unhashable:func, inputs=[Unhashable(data=['y', 'z'])], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
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
    ...<3 lines>...
        attributes={} if attributes is None else attributes,
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

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```