## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


run(__name__, func1, verbose=True)

```

## Output

```text
Node:__main__:func1 --> io-0

```

## Warnings

```text
UserWarning: 'func1' in module '__main__' was provided more than once. Duplicates are ignored.
```

## Logging

```text
INFO	ordeq.runner	Running node 'func1' in module '__main__'
INFO	ordeq.io	Saving 'x' in module '__main__'
DEBUG	ordeq.io	Persisting data for 'x' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for 'x' in module '__main__'

```