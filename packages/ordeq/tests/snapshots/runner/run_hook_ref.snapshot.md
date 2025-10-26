## Resource

```python
from ordeq import run

run(
    "packages.example",
    hooks=["packages.example.hooks:MyHook"]
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