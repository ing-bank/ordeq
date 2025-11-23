## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

x = StringBuffer("x")
y = StringBuffer("y")
z = StringBuffer("z")
one = StringBuffer("1")


@node(inputs=[x, y], outputs=[z, one])
def func1(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(func1.attributes)


@node(inputs=[x, y], outputs=[z, one], tags=["tag1", "tag2"])
def func2(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(func2)
print(func2.attributes)


@node(inputs=[x, y], outputs=[z, one], key1="value1")
def func3(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(func3.attributes)


@node(inputs=[x, y], outputs=[z, one], attributes=None)
def func4(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


print(func4.attributes)

```

## Output

```text
{}
Node(func=__main__:func2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)], attributes={'tags': ['tag1', 'tag2']})
{'tags': ['tag1', 'tag2']}
{'key1': 'value1'}
{'attributes': None}

```