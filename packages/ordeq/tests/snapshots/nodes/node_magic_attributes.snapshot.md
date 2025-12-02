## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer


@node(
    inputs=[StringBuffer("x"), StringBuffer("y")],
    outputs=[StringBuffer("z"), StringBuffer("1")],
)
def func(x: str, y: str) -> tuple[str, str]:
    """A really nice node"""

    return f"{x} + {y}", y


print(func.__doc__)
print(func)
print(func.__annotations__)
print(func.__module__)
print("Should all print long representation:")
print(f"{func!r}")
print(repr(func))

```

## Output

```text
A really nice node
node 'func' in module '__main__'
{'x': <class 'str'>, 'y': <class 'str'>, 'return': tuple[str, str]}
ordeq._nodes
Should all print long representation:
Node(module=__main__, name=func, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
Node(module=__main__, name=func, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)])

```