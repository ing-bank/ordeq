## Resource

```python
import example_project
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_project)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=False)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Literal"}
		L02@{shape: rect, label: "Print"}
		L03@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> IO1
	IO2 --> example_project.nodes:func
	example_project.nodes:func --> IO3
	IO4 --> example_project.nodes_import:func_a
	IO5 --> example_project.nodes_import:func_a
	example_project.nodes_import:func_a --> IO6
	IO4 --> example_project.nodes_import:func_b
	IO5 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> IO7
	IO4 --> example_project.nodes_import_alias:func
	IO5 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> IO8
	IO4 --> example_project.nodes_import_reassign:func_a
	IO5 --> example_project.nodes_import_reassign:func_a
	example_project.nodes_import_reassign:func_a --> IO9
	IO4 --> example_project.nodes_import_reassign:func_b
	IO5 --> example_project.nodes_import_reassign:func_b
	example_project.nodes_import_reassign:func_b --> IO10
	IO11 --> example_project.nodes_with_inline_io:greet
	example_project.nodes_with_inline_io:greet --> IO12
	IO13 --> example_project.nodes_with_view:farewell
	example_project.nodes_with_view:farewell --> IO14
	IO15 --> example_project.nodes_with_view:greet
	example_project.nodes_with_view:greet --> IO13

	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_a@{shape: rounded, label: "func_a"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	example_project.nodes_import_reassign:func_a@{shape: rounded, label: "func_a"}
	example_project.nodes_import_reassign:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_with_inline_io:greet@{shape: rounded, label: "greet"}
	example_project.nodes_with_view:farewell@{shape: rounded, label: "farewell"}
	example_project.nodes_with_view:greet@{shape: rounded, label: "greet"}
	IO13@{shape: rect, label: "&lt;anonymous&gt;"}
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}
	IO10@{shape: rect, label: "j"}
	IO11@{shape: rect, label: "&lt;anonymous&gt;"}
	IO12@{shape: rect, label: "&lt;anonymous&gt;"}
	IO14@{shape: rect, label: "printer"}
	IO15@{shape: rect, label: "greeting"}
	IO2@{shape: rect, label: "x"}
	IO3@{shape: rect, label: "y"}
	IO4@{shape: rect, label: "a"}
	IO5@{shape: rect, label: "b"}
	IO6@{shape: rect, label: "f"}
	IO7@{shape: rect, label: "g"}
	IO8@{shape: rect, label: "h"}
	IO9@{shape: rect, label: "i"}

	class L0,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_a,example_project.nodes_import:func_b,example_project.nodes_import_alias:func,example_project.nodes_import_reassign:func_a,example_project.nodes_import_reassign:func_b,example_project.nodes_with_inline_io:greet,example_project.nodes_with_view:farewell,example_project.nodes_with_view:greet node
	class L00,IO13,IO0,IO12,IO2 io0
	class L01,IO11,IO15,IO4 io1
	class L02,IO1,IO10,IO14,IO3,IO6,IO7,IO8,IO9 io2
	class L03,IO5 io3
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