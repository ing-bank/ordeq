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
NodeResourceGraph(edges={Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>))], Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH3>))], View(name=__main__:noop): [Resource(value=IO(id=ID1))], Resource(value=Literal(12345)): [Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): [Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)): [Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH3>)): [], Resource(value=IO(id=ID1)): []})

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:noop'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(12345)
INFO	ordeq.runner	Running node "increment" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "noop" in module "__main__"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "decrement" in module "resources.runner.example_module_a"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```