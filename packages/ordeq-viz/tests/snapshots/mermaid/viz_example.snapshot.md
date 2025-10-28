## Resource

```python
from ordeq._nodes import get_node

from ordeq_viz.to_mermaid import pipeline_to_mermaid

from example import nodes as mod  # ty: ignore[unresolved-import]

diagram = pipeline_to_mermaid(
    nodes={("example", "world"): get_node(mod.world)},
    ios={("...", "x"): mod.x, ("...", "y"): mod.y},
)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph objects["Objects"]
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph io_types["IO Types"]
			ordeq_common.io.string_buffer:StringBuffer[("StringBuffer")]:::io0
		end
	end

	...:x --> example:world
	example:world --> ...:y

	subgraph pipeline["Pipeline"]
		direction TB
		example:world(["world"]):::node
		...:x[("x")]:::io0
		...:y[("y")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Typing

```text
packages/ordeq-viz/tests/resources/mermaid/viz_example.py:5: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/mermaid/viz_example.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```