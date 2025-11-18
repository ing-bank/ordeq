## Resource

```python
from ordeq_viz import viz

result = viz("example_1", fmt="mermaid-md", output=None, block_char=":")
print(result)

```

## Output

```text
:::mermaid
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

	IO0 --> example_1.wrapped_io:hello
	example_1.wrapped_io:hello --> IO1
	IO1 --> example_1.wrapped_io:print_message
	example_1.wrapped_io:print_message --> IO2
	IO3 --> example_1.nodes:world
	example_1.nodes:world --> IO4
	IO5 --> example_1.pipeline:transform_input
	example_1.pipeline:transform_input --> IO6
	IO7 --> example_1.pipeline:transform_mock_input
	example_1.pipeline:transform_mock_input --> IO8

	example_1.wrapped_io:hello@{shape: rounded, label: "hello"}
	example_1.wrapped_io:print_message@{shape: rounded, label: "print_message"}
	IO1@{shape: rect, label: "message"}
	example_1.nodes:world@{shape: rounded, label: "world"}
	example_1.pipeline:transform_input@{shape: rounded, label: "transform_input"}
	example_1.pipeline:transform_mock_input@{shape: rounded, label: "transform_mock_input"}
	IO0@{shape: rect, label: "name_generator"}
	IO2@{shape: rect, label: "name_printer"}
	IO3@{shape: rect, label: "x"}
	IO4@{shape: rect, label: "y"}
	IO5@{shape: rect, label: "TestInput"}
	IO6@{shape: rect, label: "TestOutput"}
	IO7@{shape: rect, label: "Hello"}
	IO8@{shape: rect, label: "World"}

	class L0,example_1.wrapped_io:hello,example_1.wrapped_io:print_message,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input node
	class L00,IO5 io0
	class L01,IO6 io1
	class L02,IO0 io2
	class L03,IO2 io3
	class L04,IO1 io4
	class L05,IO3,IO4,IO7,IO8 io5
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f

:::


```