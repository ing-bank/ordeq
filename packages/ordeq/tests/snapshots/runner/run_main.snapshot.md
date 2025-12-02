## Resource

```python
import logging

from ordeq import IO, node, run

io1 = IO[str]()
io2 = IO[str]()


@node(outputs=io1)
def hello():
    return "Hello"


@node(inputs=io1, outputs=io2)
def greet(name: str):
    return f"{name}, World!"


logging.basicConfig(level=logging.INFO)
assert __name__ == "__main__"
run(__name__)

```

## Output

```text
IOException: Failed to load IO 'io1' in module '__main__'.

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

  File "/packages/ordeq/tests/resources/runner/run_main.py", line LINO, in <module>
    run(__name__)
    ~~~^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.runner	Running IO 'io1' in module '__main__'
INFO	ordeq.io	Loading IO 'io1' in module '__main__'

```