## Resource

```python
import logging

from ordeq import IO, node, run

io1 = IO()
io2 = IO()


@node(outputs=io1)
def hello():
    return "Hello"


@node(inputs=io1, outputs=io2)
def greet(name: str):
    return f"{name}, World!"


logging.basicConfig(level=logging.INFO)
assert __name__ == "__main__"
run(__name__)

```

## Logging

```text
INFO	ordeq.runner	Running node '__main__:hello'
INFO	ordeq.runner	Running node '__main__:greet'

```