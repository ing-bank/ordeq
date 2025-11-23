## Resource

```python
from example_1 import nodes as mod

from ordeq_viz.graph import _gather_graph
from ordeq_viz.to_mermaid import graph_to_mermaid

diagram = graph_to_mermaid(
    _gather_graph(nodes=[mod.world], ios={"...": {"x": mod.x, "y": mod.y}})
)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_1.nodes:world
	example_1.nodes:world --> IO1

	example_1.nodes:world@{shape: rounded, label: "world"}
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}

	class L0,example_1.nodes:world node
	class L00,IO0,IO1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```