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
View:View(func=__main__:print_message, ...) --> io-1
Hello from printer
View:View(func=__main__:print_message, ...) --> io-1
Hello from printer

```

## Logging

```text
INFO	ordeq.runner	Running View(func=__main__:print_message, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running View(func=__main__:print_message, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```