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
  File "/packages/ordeq-common/tests/resources/hooks/spy_hook.py", line LINO, in fail
    raise ValueError("Intentional failure for testing.")

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapper
    return func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(patched_nodes[node], hooks=hooks, save=save_node)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=io)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-common/tests/resources/hooks/spy_hook.py", line LINO, in <module>
    run(fail, hooks=[spy])
    ~~~^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
[('before_node_run', Node(name=spy_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)])), ('after_node_run', Node(name=spy_hook:hello, inputs=[Literal('name')], outputs=[IO(idx=ID1)]))]

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'spy_hook:fail'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('name')
INFO	ordeq.runner	Running node "hello" in module "spy_hook"
INFO	ordeq.runner	Running view "fail" in module "spy_hook"

```