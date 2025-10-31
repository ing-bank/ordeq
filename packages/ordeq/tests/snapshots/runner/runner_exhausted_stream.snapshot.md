## Resource

```python
from collections.abc import Generator, Iterable
from dataclasses import dataclass, field

from ordeq import IO, node
from ordeq._runner import run
from ordeq_common import Literal


@dataclass(eq=False)
class Stream(IO[Generator[str, None, None]]):
    data: Iterable[str] = field(default_factory=list, hash=False)

    def load(self) -> Generator[str, None, None]:
        for item in self.data:
            yield from item

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

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/runner_exhausted_stream.py", line LINO, in <module>
    run(increment, multiply, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     runner_exhausted_stream:increment -> [runner_exhausted_stream:multiply]
     runner_exhausted_stream:multiply -> []
  Nodes:
     runner_exhausted_stream:increment: Node(name=runner_exhausted_stream:increment, inputs=[Stream(data=['1', '2', '3'])], outputs=[Stream(data=[])])
     runner_exhausted_stream:multiply: Node(name=runner_exhausted_stream:multiply, inputs=[Stream(data=[]), Literal('2')], outputs=[Stream(data=[])])

```

## Typing

```text
packages/ordeq/tests/resources/runner/runner_exhausted_stream.py:19: error: Unsupported left operand type for + ("Iterable[str]")  [operator]
Found 1 error in 1 file (checked 1 source file)

```