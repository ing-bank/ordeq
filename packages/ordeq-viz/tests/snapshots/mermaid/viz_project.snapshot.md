## Resource

```python
import example_project

from ordeq_viz import viz

diagram = viz(example_project, fmt="mermaid", subgraphs=False)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Literal"}
		L02@{shape: rect, label: "Print"}
		L03@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_project.nodes_with_view:greet
	example_project.nodes_with_view:greet --> example_project.nodes_with_view:farewell
	example_project.nodes_with_view:farewell --> IO1
	IO2 --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> IO3
	IO4 --> example_project.nodes:func
	example_project.nodes:func --> IO5
	IO6 --> example_project.nodes_import:func_a
	IO7 --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> IO8
	IO6 --> example_project.nodes_import:func_b
	IO7 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> IO9
	IO6 --> example_project.nodes_import_alias:func
	IO7 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> IO10
	IO11 --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> IO12

	example_project.nodes_with_view:greet@{shape: subroutine, label: "greet"}
	example_project.nodes_with_view:farewell@{shape: rounded, label: "farewell"}
	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_a@{shape: rounded, label: "func_a"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	example_project.nodes_with_inline_io:greet@{shape: rounded, label: "greet"}
	IO0@{shape: rect, label: "greeting"}
	IO1@{shape: rect, label: "printer"}
	IO10@{shape: rect, label: "h"}
	IO11@{shape: rect, label: "&lt;anonymous&gt;"}
	IO12@{shape: rect, label: "&lt;anonymous&gt;"}
	IO2@{shape: rect, label: "x"}
	IO3@{shape: rect, label: "y"}
	IO4@{shape: rect, label: "x"}
	IO5@{shape: rect, label: "y"}
	IO6@{shape: rect, label: "a"}
	IO7@{shape: rect, label: "B"}
	IO8@{shape: rect, label: "f"}
	IO9@{shape: rect, label: "g"}

	class L0,example_project.nodes_with_view:farewell,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_a,example_project.nodes_import:func_b,example_project.nodes_import_alias:func,example_project.nodes_with_inline_io:greet node
	class L2,example_project.nodes_with_view:greet view
	class L00,IO12,IO2,IO4 io0
	class L01,IO0,IO11,IO6 io1
	class L02,IO1,IO10,IO3,IO5,IO8,IO9 io2
	class L03,IO7 io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```