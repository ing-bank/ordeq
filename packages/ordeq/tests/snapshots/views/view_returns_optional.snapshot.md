## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> None | str:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: None | str):
    return v


glob = 3
print(run(n, verbose=True))

glob = 1
print(run(n, verbose=True))

```

## Output

```text
NodeGraph:
  Edges:
     view_returns_optional:conditional -> [view_returns_optional:n]
     view_returns_optional:n -> []
  Nodes:
     view_returns_optional:conditional: View(name=view_returns_optional:conditional)
     view_returns_optional:n: Node(name=view_returns_optional:n, inputs=[View(name=view_returns_optional:conditional)], outputs=[Print()])
Higher value!
{View(name=view_returns_optional:conditional): 'Higher value!', Print(): 'Higher value!'}
NodeGraph:
  Edges:
     view_returns_optional:conditional -> [view_returns_optional:n]
     view_returns_optional:n -> []
  Nodes:
     view_returns_optional:conditional: View(name=view_returns_optional:conditional)
     view_returns_optional:n: Node(name=view_returns_optional:n, inputs=[View(name=view_returns_optional:conditional)], outputs=[Print()])
None
{View(name=view_returns_optional:conditional): None, Print(): None}

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