## Resource

```python
import example_1

from ordeq_viz import viz

diagram = viz(example_1, fmt="mermaid", subgraphs=True)
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

	example_1.wrapped_io:name_generator --> example_1.wrapped_io:hello
	example_1.wrapped_io:hello --> example_1.wrapped_io:message
	example_1.wrapped_io:message --> example_1.wrapped_io:print_message
	example_1.wrapped_io:print_message --> example_1.wrapped_io:name_printer
	example_1.nodes:x --> example_1.nodes:world
	example_1.nodes:world --> example_1.nodes:y
	unknown_0 --> example_1.pipeline:transform_input
	example_1.pipeline:transform_input --> unknown_1
	unknown_2 --> example_1.pipeline:transform_mock_input
	example_1.pipeline:transform_mock_input --> unknown_3

	subgraph s0["example_1.wrapped_io"]
		direction TB
		example_1.wrapped_io:hello@{shape: rounded, label: "hello"}
		example_1.wrapped_io:print_message@{shape: rounded, label: "print_message"}
		example_1.wrapped_io:message@{shape: rect, label: "message"}
	end
	subgraph s1["example_1.nodes"]
		direction TB
		example_1.nodes:world@{shape: rounded, label: "world"}
	end
	subgraph s2["example_1.pipeline"]
		direction TB
		example_1.pipeline:transform_input@{shape: rounded, label: "transform_input"}
		example_1.pipeline:transform_mock_input@{shape: rounded, label: "transform_mock_input"}
	end
	example_1.nodes:x@{shape: rect, label: "x"}
	example_1.nodes:y@{shape: rect, label: "y"}
	example_1.wrapped_io:name_generator@{shape: rect, label: "name_generator"}
	example_1.wrapped_io:name_printer@{shape: rect, label: "name_printer"}
	unknown_0@{shape: rect, label: "TestInput"}
	unknown_1@{shape: rect, label: "TestOutput"}
	unknown_2@{shape: rect, label: "Hello"}
	unknown_3@{shape: rect, label: "World"}

	class L0,example_1.wrapped_io:hello,example_1.wrapped_io:print_message,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input node
	class L00,unknown_0 io0
	class L01,unknown_1 io1
	class L02,example_1.wrapped_io:name_generator io2
	class L03,example_1.wrapped_io:name_printer io3
	class L04,example_1.wrapped_io:message io4
	class L05,example_1.nodes:x,example_1.nodes:y,unknown_2,unknown_3 io5
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f


```

## Logging

```text
WARNING	ordeq.preview	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```