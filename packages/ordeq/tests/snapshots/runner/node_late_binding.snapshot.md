## Resource

```python
from ordeq import node


# this does not raise an error, only on `run`
@node
def func(x: str) -> str:
    return x

```