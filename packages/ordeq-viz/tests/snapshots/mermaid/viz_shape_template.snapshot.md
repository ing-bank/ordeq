## Resource

```python
from example_1 import nodes as mod

from ordeq_viz.graph import _gather_graph
from ordeq_viz.to_mermaid import graph_to_mermaid

diagram = graph_to_mermaid(
    _gather_graph(nodes=[mod.world], ios={"...": {"x": mod.x, "y": mod.y}}),
    io_shape="manual-input",
    node_shape="manual-file",
)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: manual-file, label: "Node"}
		L00@{shape: manual-input, label: "StringBuffer"}
	end

	example_1.nodes:x --> example_1.nodes:world
	example_1.nodes:world --> example_1.nodes:y

	example_1.nodes:world@{shape: manual-file, label: "world"}
	example_1.nodes:x@{shape: manual-input, label: "x"}
	example_1.nodes:y@{shape: manual-input, label: "y"}

	class L0,example_1.nodes:world node
	class L00,example_1.nodes:x,example_1.nodes:y io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```