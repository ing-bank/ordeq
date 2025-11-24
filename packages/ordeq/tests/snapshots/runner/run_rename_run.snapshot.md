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
View:View(func=__main__:print_message, ...) --> io-0
Hello from printer
View:View(func=__main__:print_message, ...) --> io-0
Hello from printer

```

## Logging

```text
INFO	ordeq.runner	Running view View(func=__main__:print_message, ...)
INFO	ordeq.runner	Running view View(func=__main__:print_message, ...)

```