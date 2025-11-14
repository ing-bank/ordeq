## Resource

```python
import tempfile
from pathlib import Path

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz("example_1", "example_2", fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "Input"}
		L01@{shape: rect, label: "MockInput"}
		L02@{shape: rect, label: "MockOutput"}
		L03@{shape: rect, label: "NameGenerator"}
		L04@{shape: rect, label: "NamePrinter"}
		L05@{shape: rect, label: "Output"}
		L06@{shape: rect, label: "SayHello"}
		L07@{shape: rect, label: "StringBuffer"}
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
	IO9 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> IO10

	example_1.nodes:world@{shape: rounded, label: "world"}
	example_1.pipeline:transform_input@{shape: rounded, label: "transform_input"}
	example_1.pipeline:transform_mock_input@{shape: rounded, label: "transform_mock_input"}
	example_1.wrapped_io:hello@{shape: rounded, label: "hello"}
	example_1.wrapped_io:print_message@{shape: rounded, label: "print_message"}
	IO7@{shape: rect, label: "message"}
	example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}
	IO10@{shape: rect, label: "TestOutput2"}
	IO2@{shape: rect, label: "TestInput"}
	IO3@{shape: rect, label: "TestOutput"}
	IO4@{shape: rect, label: "Hello"}
	IO5@{shape: rect, label: "World"}
	IO6@{shape: rect, label: "name_generator"}
	IO8@{shape: rect, label: "name_printer"}
	IO9@{shape: rect, label: "TestInput2"}

	class L0,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input,example_1.wrapped_io:hello,example_1.wrapped_io:print_message,example_2.nodes:transform_input_2 node
	class L00,IO9 io0
	class L01,IO2 io1
	class L02,IO3 io2
	class L03,IO6 io3
	class L04,IO8 io4
	class L05,IO10 io5
	class L06,IO7 io6
	class L07,IO0,IO1,IO4,IO5 io7
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f
	classDef io6 fill:#e5c494
	classDef io7 fill:#b3b3b3


```