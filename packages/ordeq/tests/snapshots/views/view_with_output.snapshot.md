## Resource

```python
from ordeq import node
from ordeq_common import Print


@node(outputs=Print())
def hello() -> str:
    return "Hello, World!"


@node(inputs=hello)
def say_hello(value: str) -> str:
    return value

```

## Exception

```text
ValueError: Input '<function hello at HASH1>' to node 'view_with_output:say_hello' is not a view
```