## Resource

```python
from ordeq import node
from ordeq._nodes import get_node


@node()
def my_view() -> None:
    print("Hello, world!")


print(repr(get_node(my_view)))

```

## Output

```text
View(func=<function my_view at HASH1>)

```