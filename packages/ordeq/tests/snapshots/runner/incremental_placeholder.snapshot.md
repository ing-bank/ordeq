## Resource

```python
from ordeq import IO, Input, Output, node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = Input[str]()
I2 = Input[str]()
O1 = IO[str]()
O2 = Output[str]()


@node(inputs=[I1, I2], outputs=O1)
def f(i: str, j: str) -> str:
    return f"{i} {j}"


@node(inputs=O1, outputs=O2)
def g(a: str) -> str:
    return f(a, a)


print(run(f, g, verbose=True))  # raises NotImplementedError

```

## Exception

```text
IOException: Failed to load Input(idx=ID1).

```

## Output

```text
NodeGraph:
  Edges:
     incremental_placeholder:f -> [incremental_placeholder:g]
     incremental_placeholder:g -> []
  Nodes:
     Node(name=incremental_placeholder:f, inputs=[Input(idx=ID1), Input(idx=ID2)], outputs=[IO(idx=ID3)])
     Node(name=incremental_placeholder:g, inputs=[IO(idx=ID3)], outputs=[Output(idx=ID4)])

```

## Logging

```text
INFO	ordeq.io	Loading Input(idx=ID1)

```