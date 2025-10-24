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

## Output

```text
HELLO FROM REMOTE!
{Print(): 'HELLO FROM REMOTE!'}

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node Node(name=overriden:func1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()])
INFO	ordeq.io	Saving Print()

```