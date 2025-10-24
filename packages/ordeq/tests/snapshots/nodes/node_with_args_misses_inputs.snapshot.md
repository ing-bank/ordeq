## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=[StringBuffer("a")])
def func(a: str) -> str:
    return a


run(func)

```

## Exception

```text
ValueError: Node inputs invalid for function arguments: Node(name=node_with_args_misses_inputs:func,...)
```