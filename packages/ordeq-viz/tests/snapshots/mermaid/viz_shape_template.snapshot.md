## Resource

```python
from example_1 import nodes as mod
from ordeq._nodes import get_node

from ordeq_viz.to_mermaid import pipeline_to_mermaid

diagram = pipeline_to_mermaid(
    nodes={get_node(mod.world)},
    ios={"...": {"x": mod.x, "y": mod.y}},
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

	IO0 --> example_1.nodes:world
	example_1.nodes:world --> IO1

	subgraph s0["example_1.nodes"]
		direction TB
		example_1.nodes:world@{shape: manual-file, label: "world"}
	end
	IO0@{shape: manual-input, label: "x"}
	IO1@{shape: manual-input, label: "y"}

	class L0,example_1.nodes:world node
	class L00,IO0,IO1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```