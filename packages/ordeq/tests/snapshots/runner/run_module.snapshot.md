## Resource

```python
from ordeq import run
from resources.runner import example_module_a

run(example_module_a, verbose=True)

```

## Output

```text
Node:resources.runner.example_module_a:increment --> io-1
io-1 --> Node:resources.runner.example_module_a:decrement
Node:resources.runner.example_module_a:decrement --> io-2
io-3 --> Node:resources.runner.example_module_a:increment
io-4 --> Node:resources.runner.example_module_a:decrement

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```