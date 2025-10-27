## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")
R1 = StringBuffer()
R2 = StringBuffer()
R3 = StringBuffer()
R4 = StringBuffer()


@node(inputs=[I1, I2], outputs=[R1])
def f1(i: str, j: str) -> str:
    return f"{i} + {j}"


@node(inputs=[I2, R1], outputs=[R2])
def f2(i: str, j: str) -> str:
    return f"{i} - {j}"


@node(inputs=[R1], outputs=[R3])
def f3(i: str) -> str:
    return f"{i} * 2"


@node(inputs=[R1, R2, R3], outputs=[R4])
def f4(i: str, j: str, k: str) -> str:
    return f"{i} / {j} + {k}"


pipeline = {f1, f2, f3, f4}

output = run(*pipeline, save="all", verbose=True)
print(output[R4])

output = run(*pipeline, save="sinks", verbose=True)
print(output[R4])

output = run(*pipeline, save="none", verbose=True)
print(output[R4])

```

## Output

```text
NodeGraph:
  Edges:
     graph:f1 -> [graph:f2, graph:f3, graph:f4]
     graph:f2 -> [graph:f4]
     graph:f3 -> [graph:f4]
     graph:f4 -> []
  Nodes:
     Node(name=graph:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     Node(name=graph:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
     Node(name=graph:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)])
     Node(name=graph:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
Hello + world! / world! - Hello + world! + Hello + world! * 2
NodeGraph:
  Edges:
     graph:f1 -> [graph:f2, graph:f3, graph:f4]
     graph:f2 -> [graph:f4]
     graph:f3 -> [graph:f4]
     graph:f4 -> []
  Nodes:
     Node(name=graph:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     Node(name=graph:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
     Node(name=graph:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)])
     Node(name=graph:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
Hello + world! / world! - Hello + world! + Hello + world! * 2
NodeGraph:
  Edges:
     graph:f1 -> [graph:f2, graph:f3, graph:f4]
     graph:f2 -> [graph:f4]
     graph:f3 -> [graph:f4]
     graph:f4 -> []
  Nodes:
     Node(name=graph:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     Node(name=graph:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
     Node(name=graph:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)])
     Node(name=graph:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
Hello + world! / world! - Hello + world! + Hello + world! * 2

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "f3" in module "graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running node "f2" in module "graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "f4" in module "graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "graph"
INFO	ordeq.runner	Running node "f3" in module "graph"
INFO	ordeq.runner	Running node "f2" in module "graph"
INFO	ordeq.runner	Running node "f4" in module "graph"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "graph"
INFO	ordeq.runner	Running node "f3" in module "graph"
INFO	ordeq.runner	Running node "f2" in module "graph"
INFO	ordeq.runner	Running node "f4" in module "graph"

```

## Typing

```text
packages/ordeq/tests/resources/runner/graph.py:35: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:38: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:41: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
Found 3 errors in 1 file (checked 1 source file)

```