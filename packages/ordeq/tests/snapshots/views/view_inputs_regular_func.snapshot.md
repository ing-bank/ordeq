## Resource

```python
from ordeq import node
from ordeq._nodes import get_node
from ordeq_common import Print


def string():
    return "I'm super lazy"


@node(inputs=string)
def func(data: str) -> str:
    return str(data.__reversed__())


@node(inputs=func, outputs=Print())
def hello(data: str) -> None:
    print(data)


print(repr(get_node(hello)))

```

## Exception

```text
ValueError: Input '<function string at HASH1>' to node 'view_inputs_regular_func:func' is not a view
```