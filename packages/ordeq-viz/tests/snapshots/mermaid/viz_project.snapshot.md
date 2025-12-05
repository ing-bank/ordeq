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
	example_project.nodes_with_inline_io:greet:hello --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> unknown_0
	example_project.catalog_1:a --> example_project.nodes_import_alias:func
	example_project.catalog_1:b --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> example_project.catalog_2:h
	example_project.catalog_1:a --> example_project.nodes_import:func_b
	example_project.catalog_1:b --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> example_project.catalog_2:g
	example_project.catalog_1:a --> example_project.nodes_import:func_a
	example_project.catalog_1:b --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> example_project.catalog_2:f
	example_project.nodes:x --> example_project.nodes:func
	example_project.nodes:func --> example_project.nodes:y
	example_project.inner.nodes:x --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> example_project.inner.nodes:y

	example_project.nodes_with_view:greet@{shape: subroutine, label: "greet"}
	example_project.nodes_with_view:farewell@{shape: rounded, label: "farewell"}
	example_project.nodes_with_inline_io:greet@{shape: rounded, label: "greet"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import:func_a@{shape: rounded, label: "func_a"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.catalog_1:a@{shape: rect, label: "a"}
	example_project.catalog_1:b@{shape: rect, label: "b"}
	example_project.catalog_2:f@{shape: rect, label: "f"}
	example_project.catalog_2:g@{shape: rect, label: "g"}
	example_project.catalog_2:h@{shape: rect, label: "h"}
	example_project.inner.nodes:x@{shape: rect, label: "x"}
	example_project.inner.nodes:y@{shape: rect, label: "y"}
	example_project.nodes:x@{shape: rect, label: "x"}
	example_project.nodes:y@{shape: rect, label: "y"}
	example_project.nodes_with_inline_io:greet:hello@{shape: rect, label: "greet:hello"}
	example_project.nodes_with_view:greeting@{shape: rect, label: "greeting"}
	example_project.nodes_with_view:printer@{shape: rect, label: "printer"}
	unknown_0@{shape: rect, label: "&lt;anonymous&gt;"}

	class node_type,example_project.nodes_with_view:farewell,example_project.nodes_with_inline_io:greet,example_project.nodes_import_alias:func,example_project.nodes_import:func_b,example_project.nodes_import:func_a,example_project.nodes:func,example_project.inner.nodes:func node
	class view_type,example_project.nodes_with_view:greet view
	class io_type_0,example_project.inner.nodes:x,example_project.nodes:x,unknown_0 io0
	class io_type_1,example_project.catalog_1:a,example_project.nodes_with_inline_io:greet:hello,example_project.nodes_with_view:greeting io1
	class io_type_2,example_project.catalog_2:f,example_project.catalog_2:g,example_project.catalog_2:h,example_project.inner.nodes:y,example_project.nodes:y,example_project.nodes_with_view:printer io2
	class io_type_3,example_project.catalog_1:b io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```