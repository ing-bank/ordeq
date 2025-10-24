## Resource

```python
from ordeq import node
from ordeq_common import Literal, StringBuffer


@node(inputs=[Literal(["y", "z"])], outputs=StringBuffer("y"))
def func(x: str) -> str:
    return x

```