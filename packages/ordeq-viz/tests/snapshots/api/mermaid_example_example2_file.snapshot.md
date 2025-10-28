## Resource

```python
from pathlib import Path
import tempfile
from ordeq_viz import viz


with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz("example", "example2", fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph objects["Objects"]
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph io_types["IO Types"]
			example.catalog:MockInput[("MockInput")]:::io0
			example.catalog:MockOutput[("MockOutput")]:::io1
			example.wrapped_io:NameGenerator[("NameGenerator")]:::io2
			example.wrapped_io:NamePrinter[("NamePrinter")]:::io3
			example.wrapped_io:SayHello[("SayHello")]:::io4
			ordeq._io:IO[("IO")]:::io5
			ordeq._io:Input[("Input")]:::io6
			ordeq._io:Output[("Output")]:::io7
			ordeq_common.io.string_buffer:StringBuffer[("StringBuffer")]:::io8
		end
	end

	example.nodes:<anonymous0> --> example.nodes:node_with_inline_io
	example.nodes:node_with_inline_io --> example.nodes:<anonymous1>
	example.nodes:x --> example.nodes:world
	example.nodes:world --> example.nodes:y
	example.pipeline:TestInput --> example.pipeline:transform_input
	example.pipeline:transform_input --> example.pipeline:TestOutput
	example.pipeline:Hello --> example.pipeline:transform_mock_input
	example.pipeline:transform_mock_input --> example.pipeline:World
	example.wrapped_io:name_generator --> example.wrapped_io:hello
	example.wrapped_io:hello --> example.wrapped_io:message
	example.wrapped_io:message --> example.wrapped_io:print_message
	example.wrapped_io:print_message --> example.wrapped_io:name_printer
	example2.catalog:TestInput2 --> example2.nodes:transform_input_2
	example2.nodes:transform_input_2 --> example2.catalog:TestOutput2

	subgraph pipeline["Pipeline"]
		direction TB
		example.nodes:node_with_inline_io(["node_with_inline_io"]):::node
		example.nodes:world(["world"]):::node
		example.pipeline:transform_input(["transform_input"]):::node
		example.pipeline:transform_mock_input(["transform_mock_input"]):::node
		example.wrapped_io:hello(["hello"]):::node
		example.wrapped_io:print_message(["print_message"]):::node
		example2.nodes:transform_input_2(["transform_input_2"]):::node
		example.catalog:Hello[("Hello")]:::io8
		example.catalog:TestInput[("TestInput")]:::io0
		example.catalog:TestOutput[("TestOutput")]:::io1
		example.catalog:World[("World")]:::io8
		example.nodes:x[("x")]:::io8
		example.nodes:y[("y")]:::io8
		example.pipeline:Hello[("Hello")]:::io8
		example.pipeline:TestInput[("TestInput")]:::io0
		example.pipeline:TestOutput[("TestOutput")]:::io1
		example.pipeline:World[("World")]:::io8
		example.wrapped_io:message[("message")]:::io4
		example.wrapped_io:name_generator[("name_generator")]:::io2
		example.wrapped_io:name_printer[("name_printer")]:::io3
		example2.catalog:TestInput2[("TestInput2")]:::io6
		example2.catalog:TestOutput2[("TestOutput2")]:::io7
		example2.nodes:TestInput2[("TestInput2")]:::io6
		example2.nodes:TestOutput2[("TestOutput2")]:::io7
		example.nodes:<anonymous0>[("&lt;anonymous0&gt;")]:::io5
		example.nodes:<anonymous1>[("&lt;anonymous1&gt;")]:::io5
	end

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
	classDef io8 fill:#ff69b4


```