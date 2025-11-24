## Resource

```python
from example_checks import pipeline_views
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_views, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_views)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Literal"}
	end

	IO0 --> example_checks.pipeline_views:Ap
	IO1 --> example_checks.pipeline_views:Bp
	example_checks.pipeline_views:Ap --> example_checks.pipeline_views:AB
	example_checks.pipeline_views:Bp --> example_checks.pipeline_views:AB
	example_checks.pipeline_views:AB --> example_checks.pipeline_views:print_result

	example_checks.pipeline_views:Ap@{shape: subroutine, label: "Ap"}
	example_checks.pipeline_views:Bp@{shape: subroutine, label: "Bp"}
	example_checks.pipeline_views:AB@{shape: subroutine, label: "AB"}
	example_checks.pipeline_views:print_result@{shape: subroutine, label: "print_result"}
	IO0@{shape: rect, label: "A"}
	IO1@{shape: rect, label: "B"}

	class L0 node
	class L2,example_checks.pipeline_views:Ap,example_checks.pipeline_views:Bp,example_checks.pipeline_views:AB,example_checks.pipeline_views:print_result view
	class L00 io0
	class L01,IO0,IO1 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

Expected output is 'aBBB'
aBBB

```

## Logging

```text
INFO	ordeq.io	Loading Literal('A')
INFO	ordeq.runner	Running view 'example_checks.pipeline_views:Ap'
INFO	ordeq.io	Loading Literal('B')
INFO	ordeq.runner	Running view 'example_checks.pipeline_views:Bp'
INFO	ordeq.runner	Running view 'example_checks.pipeline_views:AB'
INFO	ordeq.runner	Running view 'example_checks.pipeline_views:print_result'

```