## Resource

```python
from types import ModuleType

from ordeq import node, run

from resources.catalog.catalogs import local, remote

catalog: ModuleType = local


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

catalog: ModuleType = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func2))

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=static:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]), Node(name=static:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])])
```

## Typing

```text
packages/ordeq/tests/resources/catalog/static.py:17: error: Name "catalog" already defined on line 7  [no-redef]
Found 1 error in 1 file (checked 1 source file)

```