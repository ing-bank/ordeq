## Resource

```python
import inspect

from ordeq import node
from ordeq._nodes import _is_node
from ordeq_common import StringBuffer


@node(
    inputs=[StringBuffer("x"), StringBuffer("y")],
    outputs=[StringBuffer("z"), StringBuffer("1")],
)
def func(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(type(func))
print(func)
print(inspect.get_annotations(func))
print(_is_node(func))

```

## Output

```text
<class 'ordeq._nodes.Node'>
Node(func=__main__:func, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
{'x': <class 'str'>, 'y': <class 'str'>, 'return': tuple[str, str]}
True

```