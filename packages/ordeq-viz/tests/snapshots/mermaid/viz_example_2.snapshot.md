## Resource

```python
import example_2
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_2)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "Input"}
		L01@{shape: rect, label: "Output"}
	end

	IO0 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> IO1

	subgraph s0["example_2.nodes"]
		direction TB
		example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	end
	IO0@{shape: rect, label: "TestInput2"}
	IO1@{shape: rect, label: "TestOutput2"}

	class L0,example_2.nodes:transform_input_2 node
	class L00,IO0 io0
	class L01,IO1 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```