## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer

mock_x = StringBuffer("X")
mock_y = StringBuffer("Y")
mock_z = StringBuffer("Z")


@node(inputs=[mock_x, mock_y], outputs=[mock_z])
def func(x: str = "X", y: str = "Y") -> str:
    return x + y


print(func("x", "y"))
print(func("x"))
print(func(x="x", y="y"))
print(func("x", y="y"))

```

## Output

```text
xy
xY
xy
xy

```