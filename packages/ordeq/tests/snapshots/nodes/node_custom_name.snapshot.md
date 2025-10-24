## Resource

```python
from ordeq import Node


def func():
    ...


node = Node.from_func(func, inputs=[], outputs=[])
print('Original:', node)

node_renamed = Node.from_func(func, name="custom-name", inputs=[], outputs=[])
print('Renamed:', node_renamed)

```

## Output

```text
Original: Node(name=node_custom_name:func)
Renamed: Node(name=custom-name)

```