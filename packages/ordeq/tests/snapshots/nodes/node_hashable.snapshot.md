## Resource

```python
from ordeq import Input, node
from ordeq_common import StringBuffer


@node(inputs=[Input(["y", "z"])], outputs=StringBuffer("y"))
def func(x: str) -> str:
    return x

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```