## Resource

```python
from ordeq import Input, node


@node(inputs=Input[str]("A!"))
def my_node(a: str, *, b: str = "Hello"):
    print(a, b)

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```