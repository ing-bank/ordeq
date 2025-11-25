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
		L01@{shape: rect, label: "Input"}
		L02@{shape: rect, label: "Print"}
		L03@{shape: rect, label: "StringBuffer"}
	end

	example_project.inner.nodes:x --> example_project.inner.nodes:func
	example_project.inner.nodes:func --> example_project.inner.nodes:y
	example_project.nodes:x --> example_project.nodes:func
	example_project.nodes:func --> example_project.nodes:y
	unknown_0 --> example_project.nodes_import:func_b
	unknown_1 --> example_project.nodes_import:func_b
	example_project.nodes_import:func_b --> example_project.catalog_2:g
	unknown_2 --> example_project.nodes_import_alias:func
	unknown_3 --> example_project.nodes_import_alias:func
	example_project.nodes_import_alias:func --> unknown_4

	example_project.inner.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes:func@{shape: rounded, label: "func"}
	example_project.nodes_import:func_b@{shape: rounded, label: "func_b"}
	example_project.nodes_import_alias:func@{shape: rounded, label: "func"}
	example_project.catalog_2:g@{shape: rect, label: "g"}
	example_project.inner.nodes:x@{shape: rect, label: "x"}
	example_project.inner.nodes:y@{shape: rect, label: "y"}
	example_project.nodes:x@{shape: rect, label: "x"}
	example_project.nodes:y@{shape: rect, label: "y"}
	unknown_0@{shape: rect, label: "a"}
	unknown_1@{shape: rect, label: "b"}
	unknown_2@{shape: rect, label: "a"}
	unknown_3@{shape: rect, label: "b"}
	unknown_4@{shape: rect, label: "h"}

	class L0,example_project.inner.nodes:func,example_project.nodes:func,example_project.nodes_import:func_b,example_project.nodes_import_alias:func node
	class L00,example_project.inner.nodes:x,example_project.nodes:x io0
	class L01,unknown_0,unknown_2 io1
	class L02,example_project.catalog_2:g,example_project.inner.nodes:y,example_project.nodes:y,unknown_4 io2
	class L03,unknown_1,unknown_3 io3
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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for Input(id=ID4)
WARNING	ordeq.preview	Node filters are in preview mode and may change without notice in future releases.

```