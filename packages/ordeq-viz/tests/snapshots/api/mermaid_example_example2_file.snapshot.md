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

	example_1.wrapped_io:name_generator --> example_1.wrapped_io:hello
	example_1.wrapped_io:hello --> example_1.wrapped_io:message
	example_1.wrapped_io:message --> example_1.wrapped_io:print_message
	example_1.wrapped_io:print_message --> example_1.wrapped_io:name_printer
	example_1.nodes:x --> example_1.nodes:world
	example_1.nodes:world --> example_1.nodes:y
	unknown_8 --> example_1.pipeline:transform_input
	example_1.pipeline:transform_input --> unknown_9
	unknown_10 --> example_1.pipeline:transform_mock_input
	example_1.pipeline:transform_mock_input --> unknown_11
	unknown_12 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> unknown_13

	example_1.wrapped_io:hello@{shape: rounded, label: "hello"}
	example_1.wrapped_io:print_message@{shape: rounded, label: "print_message"}
	example_1.wrapped_io:message@{shape: rect, label: "message"}
	example_1.nodes:world@{shape: rounded, label: "world"}
	example_1.pipeline:transform_input@{shape: rounded, label: "transform_input"}
	example_1.pipeline:transform_mock_input@{shape: rounded, label: "transform_mock_input"}
	example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	example_1.nodes:x@{shape: rect, label: "x"}
	example_1.nodes:y@{shape: rect, label: "y"}
	example_1.wrapped_io:name_generator@{shape: rect, label: "name_generator"}
	example_1.wrapped_io:name_printer@{shape: rect, label: "name_printer"}
	unknown_10@{shape: rect, label: "Hello"}
	unknown_11@{shape: rect, label: "World"}
	unknown_12@{shape: rect, label: "TestInput2"}
	unknown_13@{shape: rect, label: "TestOutput2"}
	unknown_8@{shape: rect, label: "TestInput"}
	unknown_9@{shape: rect, label: "TestOutput"}

	class L0,example_1.wrapped_io:hello,example_1.wrapped_io:print_message,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input,example_2.nodes:transform_input_2 node
	class L00,unknown_12 io0
	class L01,unknown_8 io1
	class L02,unknown_9 io2
	class L03,example_1.wrapped_io:name_generator io3
	class L04,example_1.wrapped_io:name_printer io4
	class L05,unknown_13 io5
	class L06,example_1.wrapped_io:message io6
	class L07,example_1.nodes:x,example_1.nodes:y,unknown_10,unknown_11 io7
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