## Resource

```python
from types import ModuleType

from example_catalogs import local, remote
from ordeq import node, run

catalog: ModuleType = local


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

catalog: ModuleType = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


run(func2)
print(catalog.result.load())

```

## Output

```text



```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```