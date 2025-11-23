## Resource

```python
from ordeq import node


@node()
def my_view() -> None:
    print("Hello, world!")


print(repr(my_view))

```

## Output

```text
View(func=__main__:my_view)

```