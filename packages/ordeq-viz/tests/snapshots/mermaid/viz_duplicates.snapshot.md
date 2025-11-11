## Resource

```python
import example_duplicates
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_duplicates)
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
		L01@{shape: rect, label: "Literal"}
	end

	example_duplicates.duplicate_node_name:<lambda> --> IO0
	IO1 --> example_duplicates.file1:foo
	example_duplicates.file1:foo --> IO2
	IO3 --> example_duplicates.file2:foo
	example_duplicates.file2:foo --> IO4

	subgraph s0["example_duplicates.duplicate_node_name"]
		direction TB
		example_duplicates.duplicate_node_name:<lambda>@{shape: rounded, label: "&lt;lambda&gt;"}
	end
	subgraph s1["example_duplicates.file1"]
		direction TB
		example_duplicates.file1:foo@{shape: rounded, label: "foo"}
	end
	subgraph s2["example_duplicates.file2"]
		direction TB
		example_duplicates.file2:foo@{shape: rounded, label: "foo"}
	end
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO1@{shape: rect, label: "x_value"}
	IO2@{shape: rect, label: "y_value"}
	IO3@{shape: rect, label: "x_value"}
	IO4@{shape: rect, label: "y_value"}

	class L0,example_duplicates.duplicate_node_name:<lambda>,example_duplicates.file1:foo,example_duplicates.file2:foo node
	class L00,IO0,IO2,IO4 io0
	class L01,IO1,IO3 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_name:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_duplicates.duplicate_node_name:<lambda>'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```