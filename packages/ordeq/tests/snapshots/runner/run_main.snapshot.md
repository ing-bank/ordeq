## Resource

```python
import logging

from ordeq import IO, node, run

io1 = IO[str]()
io2 = IO[str]()


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
INFO	ordeq.runner	Running node 'hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'io1' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'io1' in module '__main__'
INFO	ordeq.runner	Running node 'greet' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'io2' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'io1' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'io2' in module '__main__'

```