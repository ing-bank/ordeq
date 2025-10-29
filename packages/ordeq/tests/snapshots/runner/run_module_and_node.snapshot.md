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
NodeGraph:
  Edges:
     resources.runner.example_module_a:decrement -> []
     resources.runner.example_module_a:increment -> [resources.runner.example_module_a:decrement]
     run_module_and_node:noop -> []
  Nodes:
     resources.runner.example_module_a:decrement: Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     resources.runner.example_module_a:increment: Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     run_module_and_node:noop: View(name=run_module_and_node:noop)

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