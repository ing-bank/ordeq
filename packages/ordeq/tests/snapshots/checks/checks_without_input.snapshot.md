## Resource

```python
from ordeq import Input, node, run
from ordeq_viz import viz

A = Input[str]("A")


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
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "Input"}
	end

	__main__:A --> __main__:dependent_node

	__main__:my_node@{shape: subroutine, label: "my_node"}
	__main__:dependent_node@{shape: subroutine, label: "dependent_node"}
	__main__:A@{shape: rect, label: "A"}

	class view_type,__main__:my_node,__main__:dependent_node view
	class io_type_0,__main__:A io0
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5

This node is required before running anything else on A
Dependent node received data: A

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running view 'my_node' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Loading Input 'A' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'A' in module '__main__'
INFO	ordeq.runner	Running view 'dependent_node' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```