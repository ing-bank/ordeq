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
		node_type@{shape: rounded, label: "Node"}
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
		io_type_2@{shape: rect, label: "Print"}
		io_type_3@{shape: rect, label: "StringBuffer"}
	end

	example_project.nodes_with_view:greeting --> example_project.nodes_with_view:greet
	example_project.nodes_with_view:greet --> example_project.nodes_with_view:farewell
	example_project.nodes_with_view:farewell --> example_project.nodes_with_view:printer
	example_project.inner.nodes:x --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> example_project.inner.nodes:y
	example_project.nodes:x --> example_project.nodes:func
	example_project.nodes:func --> example_project.nodes:y
	unknown_1 --> example_project.nodes_import:func_a
	unknown_2 --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> unknown_3
	unknown_1 --> example_project.nodes_import:func_b
	unknown_2 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> example_project.catalog_2:g
	unknown_1 --> example_project.nodes_import_alias:func
	unknown_2 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> unknown_4
	unknown_5 --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> unknown_6

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
	unknown_2@{shape: rect, label: "b"}
	unknown_3@{shape: rect, label: "f"}
	unknown_4@{shape: rect, label: "h"}
	unknown_5@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_6@{shape: rect, label: "&lt;anonymous&gt;"}

	class node_type,example_project.nodes_with_view:farewell,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_a,example_project.nodes_import:func_b,example_project.nodes_import_alias:func,example_project.nodes_with_inline_io:greet node
	class view_type,example_project.nodes_with_view:greet view
	class io_type_0,example_project.inner.nodes:x,example_project.nodes:x,unknown_6 io0
	class io_type_1,example_project.nodes_with_view:greeting,unknown_1,unknown_5 io1
	class io_type_2,example_project.catalog_2:g,example_project.inner.nodes:y,example_project.nodes:y,example_project.nodes_with_view:printer,unknown_3,unknown_4 io2
	class io_type_3,unknown_2 io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```