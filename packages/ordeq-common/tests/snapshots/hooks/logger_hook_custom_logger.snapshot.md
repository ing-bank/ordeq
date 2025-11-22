## Resource

```python
import logging

from ordeq import IO, node, run
from ordeq_common import Literal, LoggerHook

_logger = logging.getLogger("custom_logger")
_logger.setLevel(logging.CRITICAL)
logger = LoggerHook(logger=_logger)


@node(inputs=Literal("name"), outputs=IO())
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
  File "/packages/ordeq-common/tests/resources/hooks/logger_hook_custom_logger.py", line LINO, in fail
    raise ValueError("Intentional failure for testing.")

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapper
    return func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    _run_node_func(node, args=_load_inputs(node.inputs), hooks=hooks),
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-common/tests/resources/hooks/logger_hook_custom_logger.py", line LINO, in <module>
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
CRITICAL	custom_logger	Called 'before_node_run' with args: (Node(name=__main__:hello, inputs=[Literal('name')], outputs=[IO(id=ID1)]),)
INFO	ordeq.io	Loading Literal('name')
INFO	ordeq.runner	Running node "hello" in module "__main__"
CRITICAL	custom_logger	Called 'after_node_run' with args: (Node(name=__main__:hello, inputs=[Literal('name')], outputs=[IO(id=ID1)]),)
CRITICAL	custom_logger	Called 'before_node_run' with args: (View(name=__main__:fail),)
INFO	ordeq.runner	Running view "fail" in module "__main__"
CRITICAL	custom_logger	Called 'on_node_call_error' with args: (View(name=__main__:fail), ValueError('Intentional failure for testing.'))

```