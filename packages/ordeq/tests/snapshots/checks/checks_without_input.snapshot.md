## Resource

```python
from ordeq import node, run
from ordeq_common import Literal
from ordeq_viz import viz

A = Literal("A")


@node(checks=[A])
def my_node():
    print("This node is required before running anything else on A")


@node(inputs=[A])
def dependent_node(data: str):
    print(f"Dependent node received data: {data}")


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "Literal"}
	end

	IO0 --> __main__:dependent_node

	__main__:my_node@{shape: subroutine, label: "my_node"}
	__main__:dependent_node@{shape: subroutine, label: "dependent_node"}
	IO0@{shape: rect, label: "A"}

	class L0 node
	class L2,__main__:my_node,__main__:dependent_node view
	class L00,IO0 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5

This node is required before running anything else on A
Dependent node received data: A

```

## Logging

```text
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running view 'my_node' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.io	Loading Literal('A')
DEBUG	ordeq.io	Persisting data for Literal('A')
INFO	ordeq.runner	Running view 'dependent_node' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for Literal('A')
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```