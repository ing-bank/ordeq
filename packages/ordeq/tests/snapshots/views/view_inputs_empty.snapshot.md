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
View(name=__main__:my_view)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:my_view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```