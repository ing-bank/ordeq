## Resource

```python
"""A node that returns a tuple to a single output."""

from ordeq import IO, node, run

io = IO[tuple[str, str]]()


@node(outputs=[io])
def node_return_tuple() -> tuple[str, str]:
    return "hello", "world"


@node(inputs=[io])
def node_consume_tuple(data: tuple[str, str]) -> None:
    print(data)


if __name__ == "__main__":
    run(node_return_tuple, node_consume_tuple)

```

## Output

```text
IOException: Failed to load IO(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

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

  File "/packages/ordeq/tests/resources/nodes/node_return_tuple.py", line LINO, in <module>
    run(node_return_tuple, node_consume_tuple)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.runner	Running IO(id=ID1)
INFO	ordeq.io	Loading IO(id=ID1)

```