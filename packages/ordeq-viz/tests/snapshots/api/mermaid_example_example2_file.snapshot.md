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
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("Input")]:::io0
			L01[("MockInput")]:::io1
			L02[("MockOutput")]:::io2
			L03[("NameGenerator")]:::io3
			L04[("NamePrinter")]:::io4
			L05[("Output")]:::io5
			L06[("SayHello")]:::io6
			L07[("StringBuffer")]:::io7
		end
	end

	IO0 --> hello
	hello --> IO1
	IO2 --> transform_input_2
	transform_input_2 --> IO3
	IO1 --> print_message
	print_message --> IO4
	IO5 --> transform_mock_input
	transform_mock_input --> IO6
	IO7 --> transform_input
	transform_input --> IO8
	IO9 --> world
	world --> IO10

	IO0 -.->|name| IO1
	IO4 -.->|writer| IO1
	subgraph pipeline["Pipeline"]
		direction TB
		hello(["hello"]):::node
		transform_input_2(["transform_input_2"]):::node
		print_message(["print_message"]):::node
		transform_mock_input(["transform_mock_input"]):::node
		transform_input(["transform_input"]):::node
		world(["world"]):::node
		IO0[("name_generator")]:::io3
		IO1[("message")]:::io6
		IO4[("name_printer")]:::io4
		IO2[("TestInput2")]:::io0
		IO3[("TestOutput2")]:::io5
		IO5[("Hello")]:::io7
		IO6[("World")]:::io7
		IO7[("TestInput")]:::io1
		IO8[("TestOutput")]:::io2
		IO9[("x")]:::io7
		IO10[("y")]:::io7
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


```