## Resource

```python
import example_3
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_3)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "IO"}
	end

	example_3.func_defs:hello --> IO0
	example_3.func_defs:hello --> IO1

	subgraph s0["example_3.func_defs"]
		direction TB
		example_3.func_defs:hello@{shape: rounded, label: "hello"}
		example_3.func_defs:hello@{shape: rounded, label: "hello"}
	end
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO1@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_3.func_defs:hello,example_3.func_defs:hello node
	class L00,IO0,IO1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Logging

```text
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```