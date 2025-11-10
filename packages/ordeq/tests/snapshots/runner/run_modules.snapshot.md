## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Output

```text
<ordeq._graph.NodeIOGraph object at HASH1>

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH7>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_modules.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```