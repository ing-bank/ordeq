## Resource

```python
import resources.runner.example_module_a as example_module_a
import resources.runner.example_module_b as example_module_b
from ordeq import run

run(example_module_a, example_module_b, verbose=True)

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])])
```

## Output

```text
NodeGraph:
  Edges:
     resources.runner.example_module_a:decrement -> []
     resources.runner.example_module_a:increment -> []
     resources.runner.example_module_b:decrement -> []
     resources.runner.example_module_b:increment -> [resources.runner.example_module_a:decrement, resources.runner.example_module_a:decrement, resources.runner.example_module_a:increment, resources.runner.example_module_b:decrement, resources.runner.example_module_b:decrement, resources.runner.example_module_b:increment]
  Nodes:
     Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])
     Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
     Node(name=resources.runner.example_module_b:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
     Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```