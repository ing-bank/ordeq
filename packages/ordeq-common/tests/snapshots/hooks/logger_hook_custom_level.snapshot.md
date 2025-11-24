## Resource

```python
import logging

from ordeq import IO, Input, node, run
from ordeq_common import LoggerHook

logger = LoggerHook(level=logging.CRITICAL)


@node(inputs=Input("name"), outputs=IO())
def hello(name: str) -> str:
    return f"Hello, {name}!"


@node
def fail() -> None:
    raise ValueError("Intentional failure for testing.")


run(hello, hooks=[logger])

run(fail, hooks=[logger])

```

## Output

```text
ValueError: Intentional failure for testing.
  File "/packages/ordeq-common/tests/resources/hooks/logger_hook_custom_level.py", line LINO, in fail
    raise ValueError("Intentional failure for testing.")

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapper
    return func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    results = _run_node_func(node, args=args, hooks=hooks)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-common/tests/resources/hooks/logger_hook_custom_level.py", line LINO, in <module>
    run(fail, hooks=[logger])
    ~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
CRITICAL	LoggerHook	Called 'before_node_run' with args: (Node(module=__main__, name=hello, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)]),)
INFO	ordeq.runner	Running node 'hello' in module '__main__'
CRITICAL	LoggerHook	Called 'after_node_run' with args: (Node(module=__main__, name=hello, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)]),)
CRITICAL	LoggerHook	Called 'before_node_run' with args: (View(func=__main__:fail),)
INFO	ordeq.runner	Running view View(func=__main__:fail, ...)
CRITICAL	LoggerHook	Called 'on_node_call_error' with args: (View(func=__main__:fail), ValueError('Intentional failure for testing.'))

```