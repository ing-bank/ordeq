## Resource

```python
import example_catalogs.remote_overridden as catalog
from ordeq import node, run


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

```

## Output

```text


```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```