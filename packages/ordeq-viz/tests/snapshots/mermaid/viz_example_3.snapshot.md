## Resource

```python
import example_3

from ordeq_viz import viz

diagram = viz(example_3, fmt="mermaid", subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
	end


	subgraph s0["example_3.func_defs"]
		direction TB
		example_3.func_defs:hello@{shape: subroutine, label: "hello"}
		example_3.func_defs:hello@{shape: subroutine, label: "hello"}
	end

	class L0 node
	class L2,example_3.func_defs:hello,example_3.func_defs:hello view
	classDef node fill:#008AD7,color:#FFF
	classDef view fill:#00C853,color:#FFF


```

## Logging

```text
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```