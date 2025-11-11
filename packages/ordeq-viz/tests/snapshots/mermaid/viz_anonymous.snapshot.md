## Resource

```python
import example_anonymous
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_anonymous)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
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

	IO0 --> example_anonymous.nodes:node_with_inline_io
	example_anonymous.nodes:node_with_inline_io --> IO1

	example_anonymous.nodes:node_with_inline_io@{shape: rounded, label: "node_with_inline_io"}
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO1@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_anonymous.nodes:node_with_inline_io node
	class L2 view
	class L00,IO0,IO1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5


```