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
HELLO FROM LOCAL!HELLO FROM LOCAL!
HELLO FROM REMOTE!HEY I AM OVERRIDING THE HELLO IO!HELLO FROM REMOTE!

```

## Logging

```text
INFO	ordeq.runner	Loading StringBuffer 'func1:hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'func1:hello' in module '__main__'
INFO	ordeq.runner	Running node 'func1' in module '__main__'
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'func1:hello' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Loading StringBuffer 'func2:hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'func2:hello' in module '__main__'
INFO	ordeq.runner	Running node 'func2' in module '__main__'
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'func2:hello' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```