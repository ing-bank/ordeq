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
     Node(name=run_rename_run:print_message)
Hello from printer
NodeGraph:
  Edges:
     run_rename_run:print_message -> []
  Nodes:
     Node(name=run_rename_run:print_message)
Hello from printer

```

## Logging

```text
INFO	ordeq.runner	Running node Node(name=run_rename_run:print_message)
INFO	ordeq.runner	Running node Node(name=run_rename_run:print_message)

```