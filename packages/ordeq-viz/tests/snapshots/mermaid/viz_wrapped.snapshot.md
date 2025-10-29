## Resource

```python
import example  # ty: ignore[unresolved-import]
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)

print("-" * 40)

diagram = pipeline_to_mermaid(
    nodes=nodes, ios=ios, connect_wrapped_datasets=False
)
print(diagram)

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
			L00[("MockInput")]:::io0
			L01[("MockOutput")]:::io1
			L02[("NameGenerator")]:::io2
			L03[("NamePrinter")]:::io3
			L04[("SayHello")]:::io4
			L05[("StringBuffer")]:::io5
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

	IO0 -.->|name| IO1
	IO2 -.->|writer| IO1
	subgraph pipeline["Pipeline"]
		direction TB
		hello(["hello"]):::node
		print_message(["print_message"]):::node
		transform_mock_input(["transform_mock_input"]):::node
		transform_input(["transform_input"]):::node
		world(["world"]):::node
		IO0[("name_generator")]:::io2
		IO1[("message")]:::io4
		IO2[("name_printer")]:::io3
		IO3[("Hello")]:::io5
		IO4[("World")]:::io5
		IO5[("TestInput")]:::io0
		IO6[("TestOutput")]:::io1
		IO7[("x")]:::io5
		IO8[("y")]:::io5
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f

----------------------------------------
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("MockInput")]:::io0
			L01[("MockOutput")]:::io1
			L02[("NameGenerator")]:::io2
			L03[("NamePrinter")]:::io3
			L04[("SayHello")]:::io4
			L05[("StringBuffer")]:::io5
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

	subgraph pipeline["Pipeline"]
		direction TB
		hello(["hello"]):::node
		print_message(["print_message"]):::node
		transform_mock_input(["transform_mock_input"]):::node
		transform_input(["transform_input"]):::node
		world(["world"]):::node
		IO0[("name_generator")]:::io2
		IO1[("message")]:::io4
		IO2[("name_printer")]:::io3
		IO3[("Hello")]:::io5
		IO4[("World")]:::io5
		IO5[("TestInput")]:::io0
		IO6[("TestOutput")]:::io1
		IO7[("x")]:::io5
		IO8[("y")]:::io5
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f


```

## Typing

```text
packages/ordeq-viz/tests/resources/mermaid/viz_wrapped.py:1: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/mermaid/viz_wrapped.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```