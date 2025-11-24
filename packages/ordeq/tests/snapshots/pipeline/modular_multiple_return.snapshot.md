## Resource

```python
# Users should be able to run runnables in idiomatic Python:
# 1. running a pipeline should be as simple as calling a function
# 2. args should be passed in-memory, not through IOs
from typing import Any

from ordeq import IO, node, pipeline

x = IO[Any]()
y1 = IO[Any]()
y2 = IO[Any]()
y3 = IO[Any]()


@node(inputs=[x])
def n1(a):
    return a + 1


@node(inputs=n1)
def n2(b):
    return b * 2


@node(inputs=n2, outputs=[y1, y2, y3])
def n3(c):
    return c - 3, c + 3, c * 3


my_pipeline = pipeline(n1, n2, n3, inputs=[x], outputs=[y1, y2, y3])

v1, v2, v3 = my_pipeline(30)
assert v1 == 59
assert v2 == 65
assert v3 == 186

```

## Logging

```text
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view 'n1' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running view 'n2' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
INFO	ordeq.runner	Running node 'n3' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID6)

```