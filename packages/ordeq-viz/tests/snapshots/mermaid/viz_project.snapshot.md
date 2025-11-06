## Resource

```python
import example_project
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_project)
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
			L00[("IO")]:::io0
			L01[("Literal")]:::io1
			L02[("Print")]:::io2
			L03[("StringBuffer")]:::io3
		end
	end

	IO0 --> greet
	greet --> IO1
	IO1 --> farewell
	farewell --> IO2
	IO3 --> greet
	greet --> IO4
	IO5 --> func_b
	IO6 --> func_b
	func_b --> IO7
	IO5 --> func_a
	IO6 --> func_a
	func_a --> IO8
	IO5 --> func
	IO6 --> func
	func --> IO9
	IO5 --> func_b
	IO6 --> func_b
	func_b --> IO10
	IO5 --> func_a
	IO6 --> func_a
	func_a --> IO11
	IO12 --> func
	func --> IO13
	IO14 --> func
	func --> IO15

	subgraph pipeline["Pipeline"]
		direction TB
		greet(["greet"]):::node
		farewell(["farewell"]):::node
		greet(["greet"]):::node
		func_b(["func_b"]):::node
		func_a(["func_a"]):::node
		func(["func"]):::node
		func_b(["func_b"]):::node
		func_a(["func_a"]):::node
		func(["func"]):::node
		func(["func"]):::node
		IO0[("greeting")]:::io1
		IO1[("&lt;anonymous&gt;")]:::io0
		IO2[("printer")]:::io2
		IO3[("&lt;anonymous&gt;")]:::io1
		IO4[("&lt;anonymous&gt;")]:::io0
		IO5[("a")]:::io1
		IO6[("b")]:::io3
		IO7[("j")]:::io2
		IO8[("i")]:::io2
		IO9[("h")]:::io2
		IO10[("g")]:::io2
		IO11[("f")]:::io2
		IO12[("x")]:::io0
		IO13[("y")]:::io2
		IO14[("x")]:::io0
		IO15[("y")]:::io2
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```