## Resource

```python
import logging

from ordeq import node, IO, run
from ordeq_common import Literal, LoggerHook

logger = LoggerHook(level=logging.CRITICAL)


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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'logger_hook_custom_level:fail'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
CRITICAL	LoggerHook	Called 'before_node_run' with args: (Node(name=logger_hook_custom_level:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]),)
INFO	ordeq.io	Loading Literal('name')
INFO	ordeq.runner	Running node Node(name=logger_hook_custom_level:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)])
CRITICAL	LoggerHook	Called 'after_node_run' with args: (Node(name=logger_hook_custom_level:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]),)
CRITICAL	LoggerHook	Called 'before_node_run' with args: (View(name=logger_hook_custom_level:fail),)
INFO	ordeq.runner	Running node View(name=logger_hook_custom_level:fail)
CRITICAL	LoggerHook	Called 'on_node_call_error' with args: (View(name=logger_hook_custom_level:fail), ValueError('Intentional failure for testing.'))

```