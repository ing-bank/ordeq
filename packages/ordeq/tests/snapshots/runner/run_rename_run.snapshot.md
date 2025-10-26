## Resource

```python
from ordeq import run, node


@node
def print_message():
    print("Hello from printer")


run(print_message, verbose=True)

show_message = print_message

run(show_message, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     run_rename_run:print_message -> []
  Nodes:
     View(name=run_rename_run:print_message)
Hello from printer
NodeGraph:
  Edges:
     run_rename_run:print_message -> []
  Nodes:
     View(name=run_rename_run:print_message)
Hello from printer

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_rename_run:print_message'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node View(name=run_rename_run:print_message)
INFO	ordeq.runner	Running node View(name=run_rename_run:print_message)

```