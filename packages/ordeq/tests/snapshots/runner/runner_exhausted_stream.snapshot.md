## Resource

```python
from dataclasses import dataclass, field
from typing import Generator, Iterable

from ordeq import node, IO
from ordeq._runner import run
from ordeq_common import Literal


@dataclass(eq=False)
class Stream(IO[Generator[str, None, None]]):
    data: Iterable[str] = field(default_factory=list, hash=False)

    def load(self) -> Generator[str, None, None]:
        for item in self.data:
            yield item

    def save(self, data: Generator[str, None, None]) -> None:
        for item in data:
            self.data += [item]


x1 = Stream(["1", "2", "3"])
x2 = Stream()
x3 = Literal("2")
x4 = Stream()


@node(inputs=x1, outputs=x2)
def increment(items: Generator[str, None, None]) -> Generator[str, None, None]:
    for item in items:
        yield str(int(item) + 1)


@node(inputs=[x2, x3], outputs=x4)
def multiply(items: Generator[str, None, None], y: str) -> Generator[
    str, None, None
]:
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
NodeGraph:
  Edges:
     runner_exhausted_stream:increment -> [runner_exhausted_stream:multiply]
     runner_exhausted_stream:multiply -> []
  Nodes:
     Node(name=runner_exhausted_stream:increment, inputs=[Stream(data=['1', '2', '3'])], outputs=[Stream(data=[])])
     Node(name=runner_exhausted_stream:multiply, inputs=[Stream(data=[]), Literal('2')], outputs=[Stream(data=[])])
NodeGraph:
  Edges:
     runner_exhausted_stream:increment -> [runner_exhausted_stream:multiply]
     runner_exhausted_stream:multiply -> []
  Nodes:
     Node(name=runner_exhausted_stream:increment, inputs=[Stream(data=['1', '2', '3'])], outputs=[Stream(data=['2', '3', '4'])])
     Node(name=runner_exhausted_stream:multiply, inputs=[Stream(data=['2', '3', '4']), Literal('2')], outputs=[Stream(data=[])])

```

## Logging

```text
INFO	ordeq.io	Loading Stream(data=['1', '2', '3'])
INFO	ordeq.runner	Running node "increment" in module "runner_exhausted_stream"
INFO	ordeq.io	Saving Stream(data=[])
INFO	ordeq.io	Loading Literal('2')
INFO	ordeq.runner	Running node "multiply" in module "runner_exhausted_stream"
INFO	ordeq.io	Saving Stream(data=[])
INFO	ordeq.io	Loading Stream(data=['1', '2', '3'])
INFO	ordeq.runner	Running node "increment" in module "runner_exhausted_stream"
INFO	ordeq.io	Loading Literal('2')
INFO	ordeq.runner	Running node "multiply" in module "runner_exhausted_stream"
INFO	ordeq.io	Saving Stream(data=[])

```

## Typing

```text
packages/ordeq/tests/resources/runner/runner_exhausted_stream.py:19: error: Unsupported left operand type for + ("Iterable[str]")  [operator]
Found 1 error in 1 file (checked 1 source file)

```