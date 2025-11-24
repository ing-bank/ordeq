## Resource

```python
# Users should be able to run runnables in idiomatic Python:
# 1. running a pipeline should be as simple as calling a function
# 2. args should be passed in-memory, not through IOs
from typing import Any

from ordeq import IO, node, pipeline

x = IO[Any]()
y = IO[Any]()


@node(inputs=[x])
def n1(a):
    return a + 1


@node(inputs=n1)
def n2(b):
    return b * 2


@node(inputs=n2, outputs=y)
def n3(c):
    return c - 3


my_pipeline = pipeline(n1, n2, n3, inputs=[x], outputs=[y])

output = my_pipeline(30)
assert output == 59

```

## Logging

```text
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.
INFO	ordeq.runner	Running view 'n1' in module '__main__'
INFO	ordeq.runner	Running view 'n2' in module '__main__'
INFO	ordeq.runner	Running node 'n3' in module '__main__'

```