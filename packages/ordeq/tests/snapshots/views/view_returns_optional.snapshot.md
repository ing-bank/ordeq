## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> str | None:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: str | None):
    return v


glob = 3
run(n, verbose=True)

glob = 1
run(n, verbose=True)

```

## Output

```text
View:View(func=__main__:conditional, ...) --> io-0
io-0 --> Node:__main__:n
Node:__main__:n --> io-1
Higher value!
View:View(func=__main__:conditional, ...) --> io-0
io-0 --> Node:__main__:n
Node:__main__:n --> io-1
None

```

## Logging

```text
DEBUG	ordeq.runner	Running View(func=__main__:conditional, ...)
DEBUG	ordeq.io	Persisting data for IO 'n:v' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n:v' in module '__main__'
DEBUG	ordeq.runner	Running node 'n' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'n:v' in module '__main__'
DEBUG	ordeq.runner	Running View(func=__main__:conditional, ...)
DEBUG	ordeq.io	Persisting data for IO 'n:v' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n:v' in module '__main__'
DEBUG	ordeq.runner	Running node 'n' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'n:v' in module '__main__'

```