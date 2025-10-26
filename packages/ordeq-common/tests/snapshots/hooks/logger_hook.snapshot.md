## Resource

```python
from ordeq import node, IO, run
from ordeq_common import SpyHook, Literal, LoggerHook

logger = LoggerHook()


@node(inputs=Literal("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[logger])

run(fail, hooks=[logger])

```

## Exception

```text
ValueError: Intentional failure for testing.
```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'logger_hook:fail'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	LoggerHook	Called 'before_node_run' with args: (Node(name=logger_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]),)
INFO	ordeq.io	Loading Literal('name')
INFO	ordeq.runner	Running node Node(name=logger_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)])
INFO	LoggerHook	Called 'after_node_run' with args: (Node(name=logger_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]),)
INFO	LoggerHook	Called 'before_node_run' with args: (View(name=logger_hook:fail),)
INFO	ordeq.runner	Running node View(name=logger_hook:fail)
INFO	LoggerHook	Called 'on_node_call_error' with args: (View(name=logger_hook:fail), ValueError('Intentional failure for testing.'))

```