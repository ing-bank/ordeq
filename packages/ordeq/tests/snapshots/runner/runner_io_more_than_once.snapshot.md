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
AttributeError: 'Literal' object has no attribute '__name__'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_package_to_ios
    modules = _resolve_packages_to_modules([(package.__name__, package)])
                                             ^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    sorted(_resolve_package_to_ios(old).items()),
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    substitution_map = _build_substitution_map(io)

  File "/packages/ordeq/tests/resources/runner/runner_io_more_than_once.py", line LINO, in <module>
    run(increment, decrement, io={x1: p1}, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
1
NodeGraph:
  Edges:
     runner_io_more_than_once:decrement -> []
     runner_io_more_than_once:increment -> [runner_io_more_than_once:decrement]
  Nodes:
     runner_io_more_than_once:decrement: Node(name=runner_io_more_than_once:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
     runner_io_more_than_once:increment: Node(name=runner_io_more_than_once:increment, inputs=[Literal(1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```

## Logging

```text
INFO	ordeq.io	Loading Literal(1)
INFO	ordeq.runner	Running node "increment" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "decrement" in module "runner_io_more_than_once"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```