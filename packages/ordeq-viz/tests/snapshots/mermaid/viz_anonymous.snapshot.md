## Resource

```python
import example_anonymous

from ordeq_viz import viz

diagram = viz(example_anonymous, fmt="mermaid")
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
	end

	example_anonymous.nodes:node_with_inline_io:_ --> example_anonymous.nodes:node_with_inline_io
	example_anonymous.nodes:node_with_inline_io --> unknown_0
	example_anonymous.node_with_var_names:add:a --> example_anonymous.node_with_var_names:add
	example_anonymous.node_with_var_names:add:b --> example_anonymous.node_with_var_names:add

	example_anonymous.nodes:node_with_inline_io@{shape: rounded, label: "node_with_inline_io"}
	example_anonymous.node_with_var_names:add@{shape: subroutine, label: "add"}
	example_anonymous.node_with_var_names:add:a@{shape: rect, label: "add:a"}
	example_anonymous.node_with_var_names:add:b@{shape: rect, label: "add:b"}
	example_anonymous.nodes:node_with_inline_io:_@{shape: rect, label: "node_with_inline_io:_"}
	unknown_0@{shape: rect, label: "&lt;anonymous&gt;"}

	class node_type,example_anonymous.nodes:node_with_inline_io node
	class view_type,example_anonymous.node_with_var_names:add view
	class io_type_0,example_anonymous.nodes:node_with_inline_io:_,unknown_0 io0
	class io_type_1,example_anonymous.node_with_var_names:add:a,example_anonymous.node_with_var_names:add:b io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)

```