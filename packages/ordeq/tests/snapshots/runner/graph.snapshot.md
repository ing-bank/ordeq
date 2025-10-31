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

run(*pipeline, save="all", verbose=True)
print(R4.load())

run(*pipeline, save="sinks", verbose=True)
print(R4.load())

run(*pipeline, save="none", verbose=True)
print(R4.load())

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/graph.py", line LINO, in <module>
    run(*pipeline, save="all", verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     graph:f1 -> [graph:f2, graph:f3, graph:f4]
     graph:f2 -> [graph:f4]
     graph:f3 -> [graph:f4]
     graph:f4 -> []
  Nodes:
     graph:f1: Node(name=graph:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     graph:f2: Node(name=graph:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
     graph:f3: Node(name=graph:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)])
     graph:f4: Node(name=graph:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])

```

## Typing

```text
packages/ordeq/tests/resources/runner/graph.py:35: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:38: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:41: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
Found 3 errors in 1 file (checked 1 source file)

```