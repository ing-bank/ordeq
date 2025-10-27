## Resource

```python
from pathlib import Path
import tempfile
from ordeq_viz import viz


with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz("example", fmt="mermaid", output=output_file)
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
			L01[("MockInput")]:::io1
			L02[("MockOutput")]:::io2
			L03[("NameGenerator")]:::io3
			L04[("NamePrinter")]:::io4
			L05[("SayHello")]:::io5
			L06[("StringBuffer")]:::io6
		end
	end

	IO0 --> hello
	hello --> IO1
	IO1 --> print_message
	print_message --> IO2
	IO3 --> transform_mock_input
	transform_mock_input --> IO4
	IO5 --> transform_input
	transform_input --> IO6
	IO7 --> world
	world --> IO8
	IO9 --> node_with_inline_io
	node_with_inline_io --> IO10

	IO0 -.->|name| IO1
	IO2 -.->|writer| IO1
	subgraph pipeline["Pipeline"]
		direction TB
		hello(["hello"]):::node
		print_message(["print_message"]):::node
		transform_mock_input(["transform_mock_input"]):::node
		transform_input(["transform_input"]):::node
		world(["world"]):::node
		node_with_inline_io(["node_with_inline_io"]):::node
		IO0[("name_generator")]:::io3
		IO1[("message")]:::io5
		IO2[("name_printer")]:::io4
		IO3[("Hello")]:::io6
		IO4[("World")]:::io6
		IO5[("TestInput")]:::io1
		IO6[("TestOutput")]:::io2
		IO7[("x")]:::io6
		IO8[("y")]:::io6
		IO9[("&lt;anonymous&gt;")]:::io0
		IO10[("&lt;anonymous&gt;")]:::io0
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