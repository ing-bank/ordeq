## Resource

```python
from ordeq import run
from resources.runner.example_module_b import renamed

# The runner information shows name 'increment' for this node.
# That's the original name. We'd like to see 'renamed' instead.
# TODO: Add a method _resolve_proxy_to_node that gets the node,
# and sets its name to the proxy's name.
run(renamed, verbose=True)

```

## Output

```text
NodeResourceGraph(edges={Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>))], Resource(value=Literal(12345)): [Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): []})

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/renamed_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner.example_module_b`
Found 1 diagnostic

```