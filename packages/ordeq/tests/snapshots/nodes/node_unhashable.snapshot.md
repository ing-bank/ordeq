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
ValueError: Node is not hashable: Node(name=node_unhashable:func, ...)
  File "/packages/ordeq/src/ordeq/_nodes.py", line 208, in _raise_if_not_hashable
    raise ValueError(
        f"Node is not hashable: Node(name={n.name}, ...)"
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line 45, in __post_init__
    _raise_if_not_hashable(self)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "<string>", line 8, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line 116, in from_func
    return cls(
        func=func,
    ...<3 lines>...
        attributes={} if attributes is None else attributes,
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 331, in wrapped
    inner.__ordeq_node__ = Node.from_func(  # type: ignore[attr-defined]
                           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        inner, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/nodes/node_unhashable.py", line 16, in <module>
    @node(inputs=[Unhashable(["y", "z"])], outputs=StringBuffer("y"))
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```