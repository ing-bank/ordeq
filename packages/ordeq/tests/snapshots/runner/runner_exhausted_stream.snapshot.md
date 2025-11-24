## Resource

```python
from collections.abc import Generator
from dataclasses import dataclass, field

from ordeq import IO, Input, node
from ordeq._runner import run


@dataclass(eq=False)
class Stream(IO[Generator[str, None, None]]):
    data: list[str] = field(default_factory=list, hash=False)

    def load(self) -> Generator[str, None, None]:
        for item in self.data:
            yield from item

    def save(self, data: Generator[str, None, None]) -> None:
        for item in data:
            self.data += [item]


x1 = Stream(["1", "2", "3"])
x2 = Stream()
x3 = Input[str]("2")
x4 = Stream()


@node(inputs=x1, outputs=x2)
def increment(items: Generator[str, None, None]) -> Generator[str, None, None]:
    for item in items:
        yield str(int(item) + 1)


@node(inputs=[x2, x3], outputs=x4)
def multiply(
    items: Generator[str, None, None], y: str
) -> Generator[str, None, None]:
    for item in items:
        yield str(int(item) * int(y))


# Saving regularly yields no data in x4, since the stream of x2 in x2.save:
run(increment, multiply, verbose=True)

# Save using save="sinks" yields data in x4, but not in x2 (now, x2 is
# (exhausted in the for loop of multiply):
run(increment, multiply, verbose=True, save="sinks")

```

## Output

```text
io-0 --> Node:__main__:increment
Node:__main__:increment --> io-2
io-1 --> Node:__main__:multiply
io-2 --> Node:__main__:multiply
Node:__main__:multiply --> io-3
io-0 --> Node:__main__:increment
Node:__main__:increment --> io-2
io-1 --> Node:__main__:multiply
io-2 --> Node:__main__:multiply
Node:__main__:multiply --> io-3

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.io	Loading Stream(data=['1', '2', '3'])
DEBUG	ordeq.io	Persisting data for Stream(data=['1', '2', '3'])
INFO	ordeq.runner	Running node 'increment' in module '__main__'
INFO	ordeq.io	Saving Stream(data=[])
DEBUG	ordeq.io	Persisting data for Stream(data=['2', '3', '4'])
DEBUG	ordeq.io	Loading cached data for Stream(data=['2', '3', '4'])
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
INFO	ordeq.runner	Running node 'multiply' in module '__main__'
INFO	ordeq.io	Saving Stream(data=[])
DEBUG	ordeq.io	Persisting data for Stream(data=[])
DEBUG	ordeq.io	Unpersisting data for Stream(data=['1', '2', '3'])
DEBUG	ordeq.io	Unpersisting data for Stream(data=['2', '3', '4'])
DEBUG	ordeq.io	Unpersisting data for Stream(data=[])
INFO	ordeq.io	Loading Stream(data=['1', '2', '3'])
DEBUG	ordeq.io	Persisting data for Stream(data=['1', '2', '3'])
INFO	ordeq.runner	Running node 'increment' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
INFO	ordeq.runner	Running node 'multiply' in module '__main__'
INFO	ordeq.io	Saving Stream(data=[])
DEBUG	ordeq.io	Persisting data for Stream(data=['4', '6', '8'])
DEBUG	ordeq.io	Unpersisting data for Stream(data=['1', '2', '3'])
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for Stream(data=['4', '6', '8'])

```