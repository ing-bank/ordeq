## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer

x = StringBuffer()


@node(outputs=x)
def func1() -> str:
    return "Hello"


@node(outputs=x)
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)

```

## Exception

```text
ValueError: Nodes '__main__:func2' and '__main__:func1' both output to StringBuffer(_buffer=<_io.StringIO object at HASH1>). Nodes cannot output to the same resource.
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    raise ValueError(msg)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(ProjectGraph.from_nodes(nodes, patches))
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    graph_with_io = NodeIOGraph.from_nodes(nodes, patches=patches)  # type: ignore[arg-type]

  File "/packages/ordeq/tests/resources/runner/runner_non_distinct_ios.py", line LINO, in <module>
    run(func1, func2, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```