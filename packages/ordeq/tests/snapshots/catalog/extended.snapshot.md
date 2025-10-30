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
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!

```

## Logging

```text
INFO	ordeq.io	Loading Literal('Hey I am overriding the hello IO')
INFO	ordeq.runner	Running node "func1" in module "extended"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```

## Typing

```text
packages/ordeq/tests/resources/catalog/extended.py:1: error: Skipping analyzing "example_catalogs.remote_overridden": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/catalog/extended.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq/tests/resources/catalog/extended.py:1: error: Skipping analyzing "example_catalogs": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 2 errors in 1 file (checked 1 source file)

```