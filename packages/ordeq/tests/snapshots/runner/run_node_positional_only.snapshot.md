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
DEBUG	ordeq.io	Persisting data for Literal('a')
INFO	ordeq.io	Loading Literal('b')
DEBUG	ordeq.io	Persisting data for Literal('b')
INFO	ordeq.runner	Running view 'my_node' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for Literal('a')
DEBUG	ordeq.io	Unpersisting data for Literal('b')
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```