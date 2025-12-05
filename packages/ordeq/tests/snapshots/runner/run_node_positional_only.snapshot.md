## Resource

```python
from ordeq import Input, node, run


@node(inputs=[Input[str]("a"), Input[str]("b")])
def my_node(a, /, b):
    print(f"a: {a}, b: {b}")


run(my_node)

```

## Output

```text
a: a, b: b

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
INFO	ordeq.runner	Loading Input 'my_node:a' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'my_node:a' in module '__main__'
INFO	ordeq.runner	Loading Input 'my_node:b' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'my_node:b' in module '__main__'
INFO	ordeq.runner	Running view 'my_node' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```