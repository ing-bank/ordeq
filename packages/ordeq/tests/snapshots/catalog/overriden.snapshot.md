## Resource

```python
from ordeq import node, run

from resources.catalog.catalogs import remote_extended

catalog = remote_extended


@node(inputs=catalog.hello, outputs=catalog.another_io)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=overriden:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]), Node(name=overriden:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()])])
```