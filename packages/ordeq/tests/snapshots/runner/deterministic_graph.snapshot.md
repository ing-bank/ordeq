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
<ordeq._graph.NodeIOGraph object at HASH1>

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