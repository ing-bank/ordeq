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
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "Input"}
		io_type_1@{shape: rect, label: "MockInput"}
		io_type_2@{shape: rect, label: "MockOutput"}
		io_type_3@{shape: rect, label: "NameGenerator"}
		io_type_4@{shape: rect, label: "NamePrinter"}
		io_type_5@{shape: rect, label: "Output"}
		io_type_6@{shape: rect, label: "SayHello"}
		io_type_7@{shape: rect, label: "StringBuffer"}
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
	unknown_4 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> unknown_5

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
	unknown_0@{shape: rect, label: "TestInput"}
	unknown_1@{shape: rect, label: "TestOutput"}
	unknown_2@{shape: rect, label: "Hello"}
	unknown_3@{shape: rect, label: "World"}
	unknown_4@{shape: rect, label: "TestInput2"}
	unknown_5@{shape: rect, label: "TestOutput2"}

	class node_type,example_1.wrapped_io:hello,example_1.wrapped_io:print_message,example_1.nodes:world,example_1.pipeline:transform_input,example_1.pipeline:transform_mock_input,example_2.nodes:transform_input_2 node
	class io_type_0,unknown_4 io0
	class io_type_1,unknown_0 io1
	class io_type_2,unknown_1 io2
	class io_type_3,example_1.wrapped_io:name_generator io3
	class io_type_4,example_1.wrapped_io:name_printer io4
	class io_type_5,unknown_5 io5
	class io_type_6,example_1.wrapped_io:message io6
	class io_type_7,example_1.nodes:x,example_1.nodes:y,unknown_2,unknown_3 io7
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