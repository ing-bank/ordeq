## Resource

```python
from ordeq import node, run
from resources.runner import example_module_a


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)

```

## Output

```text
Node:resources.runner.example_module_a:decrement --> io-1
Node:resources.runner.example_module_a:increment --> io-2
io-2 --> Node:resources.runner.example_module_a:decrement
View:run_module_and_node:noop --> io-3
io-4 --> Node:resources.runner.example_module_a:decrement
io-5 --> Node:resources.runner.example_module_a:increment

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_module_and_node:noop'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "noop" in module "run_module_and_node"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```