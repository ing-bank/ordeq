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
Name: John
Name: John
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("IO")]:::io0
			L01[("Input")]:::io1
			L02[("MockInput")]:::io2
			L03[("MockOutput")]:::io3
			L04[("NameGenerator")]:::io4
			L05[("NamePrinter")]:::io5
			L06[("Output")]:::io6
			L07[("SayHello")]:::io7
			L08[("StringBuffer")]:::io8
		end
	end

	IO0 --> example.wrapped_io.hello
	example.wrapped_io.hello --> IO1
	IO2 --> example2.nodes.transform_input_2
	example2.nodes.transform_input_2 --> IO3
	IO1 --> example.wrapped_io.print_message
	example.wrapped_io.print_message --> IO4
	IO5 --> example.pipeline.transform_mock_input
	example.pipeline.transform_mock_input --> IO6
	IO7 --> example.pipeline.transform_input
	example.pipeline.transform_input --> IO8
	IO9 --> example.nodes.world
	example.nodes.world --> IO10
	IO11 --> example.nodes.node_with_inline_io
	example.nodes.node_with_inline_io --> IO12

	IO0 -.->|name| IO1
	IO4 -.->|writer| IO1
	subgraph pipeline["Pipeline"]
		direction TB
		example.wrapped_io.hello(["hello"]):::node
		example2.nodes.transform_input_2(["transform_input_2"]):::node
		example.wrapped_io.print_message(["print_message"]):::node
		example.pipeline.transform_mock_input(["transform_mock_input"]):::node
		example.pipeline.transform_input(["transform_input"]):::node
		example.nodes.world(["world"]):::node
		example.nodes.node_with_inline_io(["node_with_inline_io"]):::node
		IO0[("name_generator")]:::io4
		IO1[("message")]:::io7
		IO4[("name_printer")]:::io5
		IO2[("TestInput2")]:::io1
		IO3[("TestOutput2")]:::io6
		IO5[("Hello")]:::io8
		IO6[("World")]:::io8
		IO7[("TestInput")]:::io2
		IO8[("TestOutput")]:::io3
		IO9[("x")]:::io8
		IO10[("y")]:::io8
		IO11[("&lt;anonymous&gt;")]:::io0
		IO12[("&lt;anonymous&gt;")]:::io0
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

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node Node(name=example.wrapped_io:hello, inputs=[NameGenerator(name='John')], outputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))])
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.runner	Running node Node(name=example.wrapped_io:print_message, inputs=[SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))], outputs=[NamePrinter()])
INFO	ordeq.io	Saving NamePrinter()

```