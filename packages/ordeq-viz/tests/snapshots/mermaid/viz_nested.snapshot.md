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
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "StringBuffer"}
	end

	example_nested.subpackage.subsubpackage.hello_relative:world_relative --> unknown_0

	subgraph s0["example_nested.subpackage.subsubpackage.hello_relative"]
		direction TB
		example_nested.subpackage.subsubpackage.hello_relative:world_relative@{shape: rounded, label: "world_relative"}
	end
	subgraph s1["example_nested.subpackage.subsubpackage.hello"]
		direction TB
		example_nested.subpackage.subsubpackage.hello:world@{shape: subroutine, label: "world"}
	end
	unknown_0@{shape: rect, label: "message"}

	class L0,example_nested.subpackage.subsubpackage.hello_relative:world_relative node
	class L2,example_nested.subpackage.subsubpackage.hello:world view
	class L00,unknown_0 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5


```

## Logging

```text
INFO	ordeq.runner	Running node 'world_relative' in module 'example_nested.subpackage.subsubpackage.hello_relative'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
WARNING	ordeq.preview	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```