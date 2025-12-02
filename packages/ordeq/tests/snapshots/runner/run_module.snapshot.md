## Resource

```python
from ordeq import run
from resources.runner import example_module_a

run(example_module_a, verbose=True)

```

## Output

```text
io-0 --> Node:resources.runner.example_module_a:decrement
io-1 --> Node:resources.runner.example_module_a:decrement
io-2 --> Node:resources.runner.example_module_a:increment
Node:resources.runner.example_module_a:decrement --> io-3
Node:resources.runner.example_module_a:increment --> io-4
ValueError: invalid literal for int() with base 10: ''
  File "/packages/ordeq/tests/resources/runner/example_module_a.py", line LINO, in decrement
    return f"{int(x) - int(y)}"
              ~~~^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in inner
    return f(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    results = _run_node_func(node, args=args, hooks=hooks)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(
    ~~~~~~~~~~^
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/runner/run_module.py", line LINO, in <module>
    run(example_module_a, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.runner	Running Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'increment:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running StringBuffer 'x2' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Loading StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for IO 'decrement:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'decrement:y' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for IO 'increment:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running node 'increment' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for IO 'decrement:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for IO 'decrement:y' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running node 'decrement' in module 'resources.runner.example_module_a'

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```