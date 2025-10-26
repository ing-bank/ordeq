## Resource

```python
from ordeq import node, run

from resources.catalog.catalogs import remote_overridden

catalog = remote_overridden


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=extended:func1, inputs=[Literal('Hey I am overriding the hello IO')], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), Node(name=extended:func1, inputs=[Literal('Hey I am overriding the hello IO')], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])])
```