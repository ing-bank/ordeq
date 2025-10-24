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
```