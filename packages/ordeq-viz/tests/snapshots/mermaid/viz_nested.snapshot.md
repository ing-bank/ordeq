## Resource

```python
import example_nested
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(example_nested)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
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


	subgraph s0["example_nested.subpackage.subsubpackage.hello"]
		direction TB
		example_nested.subpackage.subsubpackage.hello:world@{shape: subroutine, label: "world"}
	end

	class L0 node
	class L2,example_nested.subpackage.subsubpackage.hello:world view
	classDef node fill:#008AD7,color:#FFF
	classDef view fill:#00C853,color:#FFF


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_nested.subpackage.subsubpackage.hello:world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```