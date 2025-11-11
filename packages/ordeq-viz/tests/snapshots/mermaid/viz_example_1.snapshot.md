## Resource

```python
import example_1
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_1)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "MockInput"}
		L01@{shape: rect, label: "MockOutput"}
		L02@{shape: rect, label: "NameGenerator"}
		L03@{shape: rect, label: "NamePrinter"}
		L04@{shape: rect, label: "SayHello"}
		L05@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_1.nodes:world
	example_1.nodes:world --> IO1
	IO2 --> example_1.pipeline:transform_input
	example_1.pipeline:transform_input --> IO3
	IO4 --> example_1.pipeline:transform_mock_input
	example_1.pipeline:transform_mock_input --> IO5
	IO6 --> example_1.wrapped_io:hello
	example_1.wrapped_io:hello --> IO7
	IO7 --> example_1.wrapped_io:print_message
	example_1.wrapped_io:print_message --> IO8

	subgraph s0["example_1.nodes"]
		direction TB
		example_1.nodes:world@{shape: rounded, label: "world"}
	end
	subgraph s1["example_1.pipeline"]
		direction TB
		example_1.pipeline:transform_input@{shape: rounded, label: "transform_input"}
		example_1.pipeline:transform_mock_input@{shape: rounded, label: "transform_mock_input"}
	end
	subgraph s2["example_1.wrapped_io"]
		direction TB
		example_1.wrapped_io:hello@{shape: rounded, label: "hello"}
		example_1.wrapped_io:print_message@{shape: rounded, label: "print_message"}
		IO7@{shape: rect, label: "message"}
	end
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}
	IO2@{shape: rect, label: "TestInput"}
	IO3@{shape: rect, label: "TestOutput"}
	IO4@{shape: rect, label: "Hello"}
	IO5@{shape: rect, label: "World"}
	IO6@{shape: rect, label: "name_generator"}
	IO8@{shape: rect, label: "name_printer"}

	class L0,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input,example_1.wrapped_io:hello,example_1.wrapped_io:print_message node
	class L2 view
	class L00,IO2 io0
	class L01,IO3 io1
	class L02,IO6 io2
	class L03,IO8 io3
	class L04,IO7 io4
	class L05,IO0,IO1,IO4,IO5 io5
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f


```

## Logging

```text
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```