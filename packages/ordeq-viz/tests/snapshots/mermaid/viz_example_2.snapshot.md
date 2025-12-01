## Resource

```python
import example_2

from ordeq_viz import viz

diagram = viz(example_2, fmt="mermaid", subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "Input"}
		io_type_1@{shape: rect, label: "Output"}
	end

	example_2.catalog:TestInput2 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> example_2.catalog:TestOutput2

	subgraph s0["example_2.nodes"]
		direction TB
		example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	end
	example_2.catalog:TestInput2@{shape: rect, label: "TestInput2"}
	example_2.catalog:TestOutput2@{shape: rect, label: "TestOutput2"}

	class node_type,example_2.nodes:transform_input_2 node
	class io_type_0,example_2.catalog:TestInput2 io0
	class io_type_1,example_2.catalog:TestOutput2 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
WARNING	ordeq.preview	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```