## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer


@node(outputs=[StringBuffer("a")])
def func() -> str:
    return "x"

```