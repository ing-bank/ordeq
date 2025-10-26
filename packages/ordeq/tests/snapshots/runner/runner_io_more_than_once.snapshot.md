## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import Literal, StringBuffer

x1 = Literal(1)
x2 = StringBuffer()
x3 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x1], outputs=x3)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


regular = run(increment, decrement, verbose=True)

print(regular)

# provide alternative IO when running the pipeline
patched = run(increment, decrement, io={x1: Literal(200)}, verbose=True)

print(patched)

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=runner_io_more_than_once:increment, inputs=[Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), Node(name=runner_io_more_than_once:increment, inputs=[Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])])
```

## Output

```text
NodeGraph:
  Edges:
     runner_io_more_than_once:decrement -> []
     runner_io_more_than_once:increment -> [runner_io_more_than_once:decrement, runner_io_more_than_once:decrement, runner_io_more_than_once:increment]
  Nodes:
     Node(name=runner_io_more_than_once:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
     Node(name=runner_io_more_than_once:increment, inputs=[Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```

## Typing

```text
packages/ordeq/tests/resources/runner/runner_io_more_than_once.py:25: error: Argument "io" to "run" has incompatible type "dict[Literal[int], Literal[int]]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

```