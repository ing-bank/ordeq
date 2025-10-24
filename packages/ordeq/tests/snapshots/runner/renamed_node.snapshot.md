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
NodeGraph:
  Edges:
     resources.runner.example_module_b:increment -> []
  Nodes:
     Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```