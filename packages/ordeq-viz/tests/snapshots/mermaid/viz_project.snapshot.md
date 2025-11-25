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
	unknown_113 --> example_project.nodes_with_view:farewell
	example_project.nodes_with_view:farewell --> example_project.nodes_with_view:printer
	example_project.inner.nodes:x --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> example_project.inner.nodes:y
	example_project.nodes:x --> example_project.nodes:func
	example_project.nodes:func --> example_project.nodes:y
	unknown_103 --> example_project.nodes_import:func_a
	unknown_104 --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> unknown_105
	unknown_106 --> example_project.nodes_import:func_b
	unknown_107 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> example_project.catalog_2:g
	unknown_108 --> example_project.nodes_import_alias:func
	unknown_109 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> unknown_110
	unknown_111 --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> unknown_112

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
	unknown_103@{shape: rect, label: "a"}
	unknown_104@{shape: rect, label: "b"}
	unknown_105@{shape: rect, label: "f"}
	unknown_106@{shape: rect, label: "a"}
	unknown_107@{shape: rect, label: "b"}
	unknown_108@{shape: rect, label: "a"}
	unknown_109@{shape: rect, label: "b"}
	unknown_110@{shape: rect, label: "h"}
	unknown_111@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_112@{shape: rect, label: "&lt;anonymous&gt;"}
	unknown_113@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_project.nodes_with_view:farewell,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_a,example_project.nodes_import:func_b,example_project.nodes_import_alias:func,example_project.nodes_with_inline_io:greet node
	class L2,example_project.nodes_with_view:greet view
	class L00,example_project.inner.nodes:x,example_project.nodes:x,unknown_112,unknown_113 io0
	class L01,example_project.nodes_with_view:greeting,unknown_103,unknown_106,unknown_108,unknown_111 io1
	class L02,example_project.catalog_2:g,example_project.inner.nodes:y,example_project.nodes:y,example_project.nodes_with_view:printer,unknown_105,unknown_110 io2
	class L03,unknown_104,unknown_107,unknown_109 io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


```