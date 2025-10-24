## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(inputs=[StringBuffer("a")])
def func(x: str) -> str:
    return x


run(func)

```

## Exception

```text
ValueError: Node outputs invalid for return annotation: Node(name=node_with_returns_misses_outputs:func,...). Node has 0 output(s), but the return type annotation expects 1 value(s).
```