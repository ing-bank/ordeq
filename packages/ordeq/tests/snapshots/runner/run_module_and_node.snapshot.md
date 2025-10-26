## Resource

```python
import resources.runner.example_module_a as example_module_a
from ordeq import run, node


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
     Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     View(name=run_module_and_node:noop)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_module_and_node:noop'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node View(name=run_module_and_node:noop)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```