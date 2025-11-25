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
		L01@{shape: rect, label: "Input"}
		L02@{shape: rect, label: "Print"}
		L03@{shape: rect, label: "StringBuffer"}
	end

	example_project.nodes_with_view:greeting --> example_project.nodes_with_view:greet
	unknown_11 --> example_project.nodes_with_view:farewell
	example_project.nodes_with_view:farewell --> example_project.nodes_with_view:printer
	example_project.inner.nodes:x --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> example_project.inner.nodes:y
	example_project.nodes:x --> example_project.nodes:func
	example_project.nodes:func --> example_project.nodes:y
	unknown_1 --> example_project.nodes_import:func_a
	unknown_2 --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> unknown_3
	unknown_4 --> example_project.nodes_import:func_b
	unknown_5 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> example_project.catalog_2:g
	unknown_6 --> example_project.nodes_import_alias:func
	unknown_7 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> unknown_8
	unknown_9 --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> unknown_10

	example_project.nodes_with_view:greet@{shape: subroutine, label: "greet"}
	example_project.nodes_with_view:farewell@{shape: rounded, label: "farewell"}
	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_a@{shape: rounded, label: "func_a"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	example_project.nodes_with_inline_io:greet@{shape: rounded, label: "greet"}
	example_project.catalog_2:g@{shape: rect, label: "g"}
	example_project.inner.nodes:x@{shape: rect, label: "x"}
	example_project.inner.nodes:y@{shape: rect, label: "y"}
	example_project.nodes:x@{shape: rect, label: "x"}
	example_project.nodes:y@{shape: rect, label: "y"}
	example_project.nodes_with_view:greeting@{shape: rect, label: "greeting"}
	example_project.nodes_with_view:printer@{shape: rect, label: "printer"}
	unknown_1@{shape: rect, label: "a"}
	unknown_10@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_11@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_2@{shape: rect, label: "b"}
	unknown_3@{shape: rect, label: "f"}
	unknown_4@{shape: rect, label: "a"}
	unknown_5@{shape: rect, label: "b"}
	unknown_6@{shape: rect, label: "a"}
	unknown_7@{shape: rect, label: "b"}
	unknown_8@{shape: rect, label: "h"}
	unknown_9@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_project.nodes_with_view:farewell,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_a,example_project.nodes_import:func_b,example_project.nodes_import_alias:func,example_project.nodes_with_inline_io:greet node
	class L2,example_project.nodes_with_view:greet view
	class L00,example_project.inner.nodes:x,example_project.nodes:x,unknown_10,unknown_11 io0
	class L01,example_project.nodes_with_view:greeting,unknown_1,unknown_4,unknown_6,unknown_9 io1
	class L02,example_project.catalog_2:g,example_project.inner.nodes:y,example_project.nodes:y,example_project.nodes_with_view:printer,unknown_3,unknown_8 io2
	class L03,unknown_2,unknown_5,unknown_7 io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```