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
Saying Hello, world!
Should run no nodes (node filter maps all nodes to False):

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Loading Input 'hello:hi' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'hello:hi' in module '__main__'
INFO	ordeq.runner	Running node 'hello' in module '__main__'
INFO	ordeq.runner	Saving StringBuffer 'world:value' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'world:value' in module '__main__'
INFO	ordeq.runner	Loading StringBuffer 'world:value' in module '__main__'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'world:value' in module '__main__'
INFO	ordeq.runner	Running view 'world' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'world:value' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.

```