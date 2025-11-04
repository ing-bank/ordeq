## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=StringBuffer())
def func1() -> str:
    return "Hello"


@node(outputs=StringBuffer())
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/runner/runner_distinct_ios.py", line LINO, in <module>
    run(func1, func2, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     runner_distinct_ios:func1 -> []
     runner_distinct_ios:func2 -> []
  Nodes:
     runner_distinct_ios:func1: Node(name=runner_distinct_ios:func1, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     runner_distinct_ios:func2: Node(name=runner_distinct_ios:func2, outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])

```