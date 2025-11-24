## Resource

```python
from ordeq import Input, node
from ordeq_common import StringBuffer


@node(inputs=(StringBuffer("a"), Input(value=4)), outputs=StringBuffer("z"))
def func(*args: str | int) -> str:
    return "".join(str(i) for i in args)


print(func("a", 4))

```

## Output

```text
a4

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```