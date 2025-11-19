## Resource

```python
import example_project

from ordeq_viz import viz

result = viz(
    example_project,
    fmt="mermaid-md",
    node_filter=lambda n: n.attributes.get("tags", "x") != "x",
    output=None,
)
print(result)

```

## Output

```text
```mermaid
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
	IO4 --> example_project.nodes_import:func_b
	IO5 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> IO6
	IO4 --> example_project.nodes_import_alias:func
	IO5 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> IO7

	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}
	IO2@{shape: rect, label: "x"}
	IO3@{shape: rect, label: "y"}
	IO4@{shape: rect, label: "a"}
	IO5@{shape: rect, label: "B"}
	IO6@{shape: rect, label: "g"}
	IO7@{shape: rect, label: "h"}

	class L0,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_b,example_project.nodes_import_alias:func node
	class L00,IO0,IO2 io0
	class L01,IO4 io1
	class L02,IO1,IO3,IO6,IO7 io2
	class L03,IO5 io3
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3

```


```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.

```