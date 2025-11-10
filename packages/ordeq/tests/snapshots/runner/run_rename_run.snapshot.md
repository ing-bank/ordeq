## Resource

```python
from ordeq import node, run


@node
def print_message():
    print("Hello from printer")


run(print_message, verbose=True)

show_message = print_message

run(show_message, verbose=True)

```

## Output

```text
<ordeq._graph.NodeIOGraph object at HASH1>
<ordeq._graph.NodeIOGraph object at HASH1>

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_rename_run:print_message'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```