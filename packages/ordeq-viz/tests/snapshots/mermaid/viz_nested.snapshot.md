## Resource

```python
import example_nested

from ordeq_viz import viz

diagram = viz(example_nested, fmt="mermaid", subgraphs=True)
print(diagram)

```

## Output

```text
Relativistic mass
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "StringBuffer"}
	end

	example_nested.subpackage.subsubpackage.hello_relative:world_relative --> unknown_1

	subgraph s0["example_nested.subpackage.subsubpackage.hello"]
		direction TB
		example_nested.subpackage.subsubpackage.hello:world@{shape: subroutine, label: "world"}
	end
	subgraph s1["example_nested.subpackage.subsubpackage.hello_relative"]
		direction TB
		example_nested.subpackage.subsubpackage.hello_relative:world_relative@{shape: rounded, label: "world_relative"}
	end
	unknown_1@{shape: rect, label: "message"}

	class node_type,example_nested.subpackage.subsubpackage.hello_relative:world_relative node
	class view_type,example_nested.subpackage.subsubpackage.hello:world view
	class io_type_0,unknown_1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5


```

## Warnings

```text
UserWarning: Node 'world_relative' in module 'example_nested.subpackage.subsubpackage.hello_relative' was provided more than once. Duplicates are ignored.
```

## Logging

```text
INFO	ordeq.runner	Running node 'world_relative' in module 'example_nested.subpackage.subsubpackage.hello_relative'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
WARNING	ordeq.preview	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```