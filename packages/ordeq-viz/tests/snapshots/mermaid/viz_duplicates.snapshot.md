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

	IO0 --> example_duplicates.file1:foo
	example_duplicates.file1:foo --> IO1
	IO2 --> example_duplicates.file2:foo
	example_duplicates.file2:foo --> IO3

	subgraph s0["example_duplicates.file1"]
		direction TB
		example_duplicates.file1:foo@{shape: rounded, label: "foo"}
	end
	subgraph s1["example_duplicates.file2"]
		direction TB
		example_duplicates.file2:foo@{shape: rounded, label: "foo"}
	end
	IO0@{shape: rect, label: "x_value"}
	IO1@{shape: rect, label: "y_value"}
	IO2@{shape: rect, label: "x_value"}
	IO3@{shape: rect, label: "y_value"}

	class L0,example_duplicates.file1:foo,example_duplicates.file2:foo node
	class L00,IO1,IO3 io0
	class L01,IO0,IO2 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B,color:#000
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```