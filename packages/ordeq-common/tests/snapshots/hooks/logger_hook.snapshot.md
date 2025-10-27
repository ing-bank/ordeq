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
  File "/packages/ordeq-common/tests/resources/hooks/logger_hook.py", line 14, in fail
    raise ValueError("Intentional failure for testing.")

  File "/packages/ordeq/src/ordeq/_nodes.py", line 454, in wrapper
    return func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line 66, in _run_node
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line 70, in _run_node
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line 134, in _run_graph
    computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)

  File "/packages/ordeq/src/ordeq/_runner.py", line 184, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq-common/tests/resources/hooks/logger_hook.py", line 19, in <module>
    run(fail, hooks=[logger])
    ~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

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