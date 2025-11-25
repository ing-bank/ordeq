## Resource

```python
import example_anonymous

from ordeq_viz import viz

diagram = viz(example_anonymous, fmt="mermaid")
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

	unknown_41 --> example_anonymous.nodes:node_with_inline_io
	example_anonymous.nodes:node_with_inline_io --> unknown_42

	example_anonymous.nodes:node_with_inline_io@{shape: rounded, label: "node_with_inline_io"}
	unknown_41@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_42@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_anonymous.nodes:node_with_inline_io node
	class L00,unknown_41,unknown_42 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```