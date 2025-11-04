## Resource

```python
from random import shuffle

from ordeq import IO, node, run

o1 = IO()
o2 = IO()
o3 = IO()
o4 = IO()


@node(outputs=o1)
def f1(): ...


@node(outputs=o2)
def f2(): ...


@node(outputs=o3)
def f3(): ...


@node(outputs=o4)
def f4(): ...


@node(inputs=[o1, o2, o3, o4])
def a(x1, x2, x3, x4): ...


@node(inputs=[o1, o2, o3, o4])
def z(x1, x2, x3, x4): ...


pipeline = {f1, f2, f3, f4, a, z}
# shuffle
x = list(pipeline)
shuffle(x)
pipeline = set(x)

run(*pipeline, verbose=True)

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/runner/deterministic_graph.py", line LINO, in <module>
    run(*pipeline, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     deterministic_graph:a -> []
     deterministic_graph:f1 -> [deterministic_graph:a, deterministic_graph:z]
     deterministic_graph:f2 -> [deterministic_graph:a, deterministic_graph:z]
     deterministic_graph:f3 -> [deterministic_graph:a, deterministic_graph:z]
     deterministic_graph:f4 -> [deterministic_graph:a, deterministic_graph:z]
     deterministic_graph:z -> []
  Nodes:
     deterministic_graph:a: View(name=deterministic_graph:a, inputs=[IO(idx=ID1), IO(idx=ID2), IO(idx=ID3), IO(idx=ID4)])
     deterministic_graph:f1: Node(name=deterministic_graph:f1, outputs=[IO(idx=ID1)])
     deterministic_graph:f2: Node(name=deterministic_graph:f2, outputs=[IO(idx=ID2)])
     deterministic_graph:f3: Node(name=deterministic_graph:f3, outputs=[IO(idx=ID3)])
     deterministic_graph:f4: Node(name=deterministic_graph:f4, outputs=[IO(idx=ID4)])
     deterministic_graph:z: View(name=deterministic_graph:z, inputs=[IO(idx=ID1), IO(idx=ID2), IO(idx=ID3), IO(idx=ID4)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'deterministic_graph:a'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'deterministic_graph:z'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```