## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


run(__name__, func1)

```

## Logging

```text
INFO	ordeq.runner	Running node 'func1' in module '__main__'
INFO	ordeq.io	Saving StringBuffer 'x' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x' in module '__main__'

```