## Resource

```python
from example_async import sync_nodes
from ordeq import run
from ordeq_viz import viz

print(viz(sync_nodes, fmt="mermaid"))
run(sync_nodes)

```

## Output

```text
graph TB


	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B


```