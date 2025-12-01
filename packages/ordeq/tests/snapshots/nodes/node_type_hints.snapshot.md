## Resource

```python
import inspect

from ordeq import node
from ordeq._nodes import _is_node
from ordeq_common import StringBuffer
from typing_extensions import reveal_type


@node(
    inputs=[StringBuffer("x"), StringBuffer("y")],
    outputs=[StringBuffer("z"), StringBuffer("1")],
)
def func(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


reveal_type(func)
print(type(func))
print(func)
print(inspect.get_annotations(func))
print(_is_node(func))

```

## Output

```text
<class 'ordeq._nodes.Node'>
node 'func' in module '__main__'
{'x': <class 'str'>, 'y': <class 'str'>, 'return': tuple[str, str]}
True

```

## Error

```text
Runtime type is 'Node'

```