## Resource

```python
from ordeq import Input, Node, node, run
from ordeq_common import Print

greeting = Input[str]("Hello")


@node(inputs=greeting, prints=False)
def hello(hi: str) -> str:
    return hi


@node(inputs=hello, outputs=Print(), prints=True)
def world(value: str) -> str:
    say = f"{value}, world!!"
    print("Saying", say)
    return say


def prints(n: Node) -> bool:
    return n.attributes.get("prints", False)


print("Should run both `hello` and `world`:")
# Even though the filter only returns True for `world`, `hello` is a view
# and is run because `world` is run.
run(hello, world, node_filter=prints, verbose=True)

print("Should run neither `hello` nor `world`:")
run(hello, node_filter=prints, verbose=True)

print("Should run both `hello` and `world`:")
run(world, node_filter=prints, verbose=True)

```

## Output

```text
Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
Saying Hello, world!!
Hello, world!!
Should run neither `hello` nor `world`:

Should run both `hello` and `world`:
io-0 --> View:__main__:hello
View:__main__:hello --> io-1
io-1 --> Node:__main__:world
Node:__main__:world --> io-2
Saying Hello, world!!
Hello, world!!

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view 'hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running node 'world' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view 'hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running node 'world' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```