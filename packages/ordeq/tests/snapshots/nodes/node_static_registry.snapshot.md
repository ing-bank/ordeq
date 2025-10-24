## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

mock_x = StringBuffer("X")
mock_z = StringBuffer("Z")


def func(x: str = "X") -> str:
    return x


@node(inputs=[mock_x], outputs=[mock_z])
def a(x):
    return func(x)


@node(inputs=[mock_x], outputs=[mock_z])
def b(x):
    return func(x)


assert a != b

```