## Resource

```python
from ordeq import Input, node, run
from ordeq_common import StringBuffer

greeting = Input[str]("Hello")
buffer = StringBuffer()


@node(inputs=greeting, outputs=buffer)
def hello(hi: str) -> str:
    print("Saying", hi)
    return hi


@node(inputs=buffer)
def world(value: str) -> str:
    say = f"{value}, world!"
    print("Saying", say)
    return say


print("Should run all nodes (node filter maps all nodes to True):")
run(hello, world, node_filter=lambda n: True)

print("Should run no nodes (node filter maps all nodes to False):")
run(hello, world, node_filter=lambda n: False)

```

## Output

```text
Should run all nodes (node filter maps all nodes to True):
Saying Hello
Saying , world!
Should run no nodes (node filter maps all nodes to False):

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
DEBUG	ordeq.runner	Running Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'hello:hi' in module '__main__'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'world:value' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'hello:hi' in module '__main__'
DEBUG	ordeq.runner	Running node 'hello' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Loading cached data for IO 'world:value' in module '__main__'
DEBUG	ordeq.runner	Running view 'world' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'world:value' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'hello:hi' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.

```