## Resource

```python
from ordeq import node, IO, run
from ordeq_common import SpyHook, Literal


spy = SpyHook()


@node(inputs=Literal("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"

@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[spy])
print(spy.called_with)

run(fail, hooks=[spy])
print(spy.called_with)

```

## Exception

```text
ValueError: Intentional failure for testing.
```

## Output

```text
[('before_node_run', Node(name=spy_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)])), ('after_node_run', Node(name=spy_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]))]

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'spy_hook:fail'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('name')
INFO	ordeq.runner	Running node Node(name=spy_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)])
INFO	ordeq.runner	Running node View(name=spy_hook:fail)

```