## Resource

```python
import example_nested
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_nested)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "IO"}
	end

	example_nested.subpackage.subsubpackage.hello:world --> IO0

	subgraph s0["example_nested.subpackage.subsubpackage.hello"]
		direction TB
		example_nested.subpackage.subsubpackage.hello:world@{shape: rounded, label: "world"}
	end
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_nested.subpackage.subsubpackage.hello:world node
	class L00,IO0 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_nested.subpackage.subsubpackage.hello:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```