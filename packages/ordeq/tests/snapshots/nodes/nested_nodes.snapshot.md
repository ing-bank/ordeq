## Resource

```python
from collections.abc import Callable

from ordeq import node
from ordeq_common import StringBuffer

mock_x = StringBuffer("X")
mock_y = StringBuffer("Y")
mock_z = StringBuffer("Z")


@node(inputs=[mock_x], outputs=[mock_z])
def func(x: str = "X") -> Callable:
    @node(inputs=[mock_y], outputs=[mock_z])
    def inner(y: str) -> str:
        return x + y

    return inner


inner_func = func()
print("Should print 'XX':")
print(inner_func("X"))
print(func)
print(inner_func)

```

## Output

```text
Should print 'XX':
XX
Node(func=__main__:func, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
Node(func=__main__:inner, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])

```