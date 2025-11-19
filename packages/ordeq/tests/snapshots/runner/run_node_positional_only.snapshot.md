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
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:my_node'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('a')
INFO	ordeq.io	Loading Literal('b')
INFO	ordeq.runner	Running view "my_node" in module "__main__"

```