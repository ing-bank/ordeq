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


run(increment, decrement, verbose=True)

print(x3.load())

# provide alternative IO when running the pipeline
p1 = Literal(200)
run(increment, decrement, io={x1: p1}, verbose=True)

print(x3.load())

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/runner_io_more_than_once.py", line LINO, in <module>
    run(increment, decrement, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     runner_io_more_than_once:decrement -> []
     runner_io_more_than_once:increment -> [runner_io_more_than_once:decrement]
  Nodes:
     runner_io_more_than_once:decrement: Node(name=runner_io_more_than_once:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
     runner_io_more_than_once:increment: Node(name=runner_io_more_than_once:increment, inputs=[Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```