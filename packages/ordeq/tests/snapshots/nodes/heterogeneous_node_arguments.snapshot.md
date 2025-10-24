## Resource

```python
from ordeq import node
from ordeq_common import Literal, StringBuffer


@node(inputs=(StringBuffer("a"), Literal(value=4)), outputs=StringBuffer("z"))
def func(*args: str | int) -> str:
    return "".join(str(i) for i in args)


print(func("a", 4))

```

## Output

```text
a4

```