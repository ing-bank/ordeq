## Resource

```python
from ordeq import IO, Input, node, run
from ordeq_common import SpyHook

spy = SpyHook()


@node(inputs=Input[str]("name"), outputs=IO())
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

## Output

```text
[('before_node_run', Node(module=__main__, name=hello, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)])), ('after_node_run', Node(module=__main__, name=hello, inputs=[Input(id=ID1)], outputs=[IO(id=ID2)]))]
ValueError: Intentional failure for testing.
  File "/packages/ordeq-common/tests/resources/hooks/spy_hook.py", line LINO, in fail
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
    _run_graph(
    ~~~~~~~~~~^
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq-common/tests/resources/hooks/spy_hook.py", line LINO, in <module>
    run(fail, hooks=[spy])
    ~~~^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
INFO	ordeq.runner	Running node 'hello' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
INFO	ordeq.runner	Running View(func=__main__:fail, ...)

```