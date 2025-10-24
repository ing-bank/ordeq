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

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): 'HEY I AM OVERRIDING THE HELLO IO!'}

```

## Logging

```text
INFO	ordeq.io	Loading Literal('Hey I am overriding the hello IO')
INFO	ordeq.runner	Running node Node(name=extended:func1, inputs=[Literal('Hey I am overriding the hello IO')], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```