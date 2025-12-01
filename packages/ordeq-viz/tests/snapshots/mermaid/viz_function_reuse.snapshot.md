## Resource

```python
import example_function_reuse

from ordeq_viz import viz

diagram = viz(example_function_reuse, fmt="mermaid")
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "StringBuffer"}
	end

	example_function_reuse.catalog:A --> example_function_reuse.nodes:a
	example_function_reuse.catalog:B --> example_function_reuse.nodes:b
	example_function_reuse.catalog:C --> example_function_reuse.nodes:c
	example_function_reuse.catalog:D --> example_function_reuse.nodes:d
	example_function_reuse.catalog:A --> example_function_reuse.nodes:pi

	example_function_reuse.nodes:a@{shape: subroutine, label: "a"}
	example_function_reuse.nodes:b@{shape: subroutine, label: "b"}
	example_function_reuse.nodes:c@{shape: subroutine, label: "c"}
	example_function_reuse.nodes:d@{shape: subroutine, label: "d"}
	example_function_reuse.nodes:pi@{shape: subroutine, label: "pi"}
	example_function_reuse.catalog:A@{shape: rect, label: "A"}
	example_function_reuse.catalog:B@{shape: rect, label: "B"}
	example_function_reuse.catalog:C@{shape: rect, label: "C"}
	example_function_reuse.catalog:D@{shape: rect, label: "D"}

	class view_type,example_function_reuse.nodes:a,example_function_reuse.nodes:b,example_function_reuse.nodes:c,example_function_reuse.nodes:d,example_function_reuse.nodes:pi view
	class io_type_0,example_function_reuse.catalog:A,example_function_reuse.catalog:B,example_function_reuse.catalog:C,example_function_reuse.catalog:D io0
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5


```