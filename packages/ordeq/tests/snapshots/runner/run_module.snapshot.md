## Resource

```python
import resources.runner.example_module_a as example_module_a
from ordeq import run

run(example_module_a, verbose=True)

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]), Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])])
```

## Output

```text
NodeGraph:
  Edges:
     resources.runner.example_module_a:decrement -> [resources.runner.example_module_a:decrement, resources.runner.example_module_a:decrement, resources.runner.example_module_a:increment]
     resources.runner.example_module_a:increment -> []
  Nodes:
     Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])

```