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
INFO	ordeq.runner	Running node "f4" in module "deterministic_graph"
INFO	ordeq.runner	Running node "f3" in module "deterministic_graph"
INFO	ordeq.runner	Running node "f2" in module "deterministic_graph"
INFO	ordeq.runner	Running node "f1" in module "deterministic_graph"
INFO	ordeq.runner	Running view "z" in module "deterministic_graph"
INFO	ordeq.runner	Running view "a" in module "deterministic_graph"

```