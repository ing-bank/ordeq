## Resource

```python
from example_catalogs import local, remote
from ordeq import node, run

env = "test-local"


def get_catalog():
    return local if env == "test-local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

env = "test-acceptance"
catalog = get_catalog()


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