## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     resources.runner.example_module_a:decrement -> []
     resources.runner.example_module_a:increment -> [resources.runner.example_module_a:decrement]
     resources.runner.example_module_b:decrement -> []
     resources.runner.example_module_b:increment -> [resources.runner.example_module_b:decrement]
  Nodes:
     resources.runner.example_module_a:decrement: Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     resources.runner.example_module_a:increment: Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     resources.runner.example_module_b:decrement: Node(name=resources.runner.example_module_b:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
     resources.runner.example_module_b:increment: Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_b"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```