## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

mock_x = StringBuffer("X")
mock_z = StringBuffer("Z")


def func(x: str = "X") -> str:
    return x


a = node(func=func, inputs=[mock_x], outputs=[mock_z])
b = node(func=func, inputs=[mock_x], outputs=[mock_z])
assert a != b

```