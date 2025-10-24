## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> None:
    print(x)

```