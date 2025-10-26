## Resource

```python
from ordeq import run
from ordeq import NodeHook


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node: {node.name}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node: {node.name}")


run(
    "packages.example",
    hooks=["packages.example.hooks:MyHook", MyHook()]
)

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=packages.example.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)]), Node(name=packages.example.nodes:world, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])])
```

## Output

```text
Starting the run

```