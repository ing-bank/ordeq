## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> str | None:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: str | None):
    return v


glob = 3
run(n, verbose=True)

glob = 1
run(n, verbose=True)

```

## Output

```text
<ordeq._graph.NodeIOGraph object at HASH1>
Higher value!
<ordeq._graph.NodeIOGraph object at HASH2>
None

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_returns_optional:conditional'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "conditional" in module "view_returns_optional"
INFO	ordeq.runner	Running node "n" in module "view_returns_optional"
INFO	ordeq.io	Saving Print()
INFO	ordeq.runner	Running view "conditional" in module "view_returns_optional"
INFO	ordeq.runner	Running node "n" in module "view_returns_optional"
INFO	ordeq.io	Saving Print()

```