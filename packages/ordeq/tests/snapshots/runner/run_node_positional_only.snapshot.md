## Resource

```python
from ordeq import node, run
from ordeq_common import Literal


@node(inputs=[Literal("a"), Literal("b")])
def my_node(a, /, b):
    print(f"a: {a}, b: {b}")


run(my_node)

```

## Output

```text
a: a, b: b

```

## Logging

```text
INFO	ordeq.io	Loading Literal('a')
INFO	ordeq.io	Loading Literal('b')
INFO	ordeq.runner	Running view "my_node" in module "__main__"

```