## Resource

```python
from ordeq._nodes import create_node


def func(): ...


node = create_node(func, inputs=[], outputs=[])
print("Original:", node)

node_renamed = create_node(func, name="custom-name", inputs=[], outputs=[])
print("Renamed:", node_renamed)

```

## Output

```text
Original: View(name=__main__:func)
Renamed: View(name=custom-name)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'custom-name'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```