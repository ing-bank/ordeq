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

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): 'HELLO FROM LOCAL!'}
{StringBuffer(_buffer=<_io.StringIO object at HASH2>): 'HELLO FROM REMOTE!'}

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node Node(name=static:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node Node(name=static:func2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```

## Typing

```text
packages/ordeq/tests/resources/catalog/static.py:17: error: Name "catalog" already defined on line 7  [no-redef]
Found 1 error in 1 file (checked 1 source file)

```