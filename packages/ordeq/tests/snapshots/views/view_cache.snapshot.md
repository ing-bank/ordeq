## Resource

```python
from ordeq import Input, node, run
from ordeq_common import StringBuffer
from functools import cache

out = StringBuffer()


@cache
def func(a: str):
    print("I'm printed only once")
    return a


a = node(func, inputs=Input("test"))
b = node(func, inputs=Input("test"))

run(a, b)

```

## Output

```text
I'm printed only once

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
INFO	ordeq.runner	Running View(func=__main__:func, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for Input(id=ID2)
INFO	ordeq.runner	Running View(func=__main__:func, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```