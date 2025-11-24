## Resource

```python
from ordeq import Input, node, run
from ordeq_common import StringBuffer

hello = Input("hello")
world = StringBuffer()


@node(inputs=hello, outputs=world)
def simple_node(hello: str) -> str:
    return hello + " world"


@node(inputs=[hello, world], checks=[hello, world])
def check_impossible(hello: str, world: str) -> None:
    print(hello, world)


if __name__ == "__main__":
    print("Expected output is an error due to impossible check")
    run(__name__)

```

## Output

```text
Expected output is an error due to impossible check
CycleError: ('nodes are in a cycle', [Node(module=__main__, name=simple_node, inputs=[Input(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), Resource(value=IO(id=ID2)), View(module=__main__, name=check_impossible, inputs=[Input(id=ID1), StringBuffer(_buffer=<_io.StringIO object at HASH1>)]), Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)), Node(module=__main__, name=simple_node, inputs=[Input(id=ID1)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])])
  File "/graphlib.py", line LINO, in prepare
    raise CycleError(f"nodes are in a cycle", cycle)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in topological_levels
    sorter.prepare()
    ~~~~~~~~~~~~~~^^

  File "/functools.py", line LINO, in __get__
    val = self.func(instance)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in topological_ordering
    return tuple(chain.from_iterable(self.topological_levels))
                                     ^^^^^^^^^^^^^^^^^^^^^^^

  File "/functools.py", line LINO, in __get__
    val = self.func(instance)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_graph
    for node in base.topological_ordering
                ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeResourceGraph.from_nodes(nodes))
           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    graph = NodeGraph.from_nodes(nodes_and_views)

  File "/packages/ordeq/tests/resources/checks/check_impossible.py", line LINO, in <module>
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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.

```