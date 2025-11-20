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
View:__main__:print_message --> io-0
Hello from printer
View:__main__:print_message --> io-0
Hello from printer

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:print_message'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "print_message" in module "__main__"
INFO	ordeq.runner	Running view "print_message" in module "__main__"

```