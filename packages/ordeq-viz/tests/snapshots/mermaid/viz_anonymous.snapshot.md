## Resource

```python
import anonymous  # ty: ignore[unresolved-import]

from ordeq._resolve import _resolve_runnables_to_nodes_and_ios
from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(anonymous)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, connect_wrapped_datasets=False)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("IO")]:::io0
		end
	end

	IO0 --> node_with_inline_io
	node_with_inline_io --> IO1

	subgraph pipeline["Pipeline"]
		direction TB
		node_with_inline_io(["node_with_inline_io"]):::node
		IO0[("&lt;anonymous&gt;")]:::io0
		IO1[("&lt;anonymous&gt;")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Typing

```text
packages/ordeq-viz/tests/resources/mermaid/viz_anonymous.py:1: error: Skipping analyzing "anonymous": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/mermaid/viz_anonymous.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```