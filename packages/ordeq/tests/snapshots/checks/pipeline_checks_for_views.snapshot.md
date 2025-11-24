## Resource

```python
from example_checks import pipeline_checks_for_views
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_checks_for_views, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_checks_for_views)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Input"}
	end

	IO0 --> example_checks.pipeline_checks_for_views:check_a
	IO1 --> example_checks.pipeline_checks_for_views:check_a
	IO0 --> example_checks.pipeline_checks_for_views:Ap
	IO2 --> example_checks.pipeline_checks_for_views:Bp
	example_checks.pipeline_checks_for_views:Ap --> example_checks.pipeline_checks_for_views:check_ap
	example_checks.pipeline_checks_for_views:Ap --> example_checks.pipeline_checks_for_views:check_join
	example_checks.pipeline_checks_for_views:Bp --> example_checks.pipeline_checks_for_views:check_join
	example_checks.pipeline_checks_for_views:Bp --> example_checks.pipeline_checks_for_views:check_bp
	example_checks.pipeline_checks_for_views:Ap --> example_checks.pipeline_checks_for_views:AB
	example_checks.pipeline_checks_for_views:Bp --> example_checks.pipeline_checks_for_views:AB
	example_checks.pipeline_checks_for_views:AB --> example_checks.pipeline_checks_for_views:check_ab
	example_checks.pipeline_checks_for_views:AB --> example_checks.pipeline_checks_for_views:print_result

	example_checks.pipeline_checks_for_views:check_a@{shape: subroutine, label: "check_a"}
	example_checks.pipeline_checks_for_views:Ap@{shape: subroutine, label: "Ap"}
	example_checks.pipeline_checks_for_views:Bp@{shape: subroutine, label: "Bp"}
	example_checks.pipeline_checks_for_views:check_ap@{shape: subroutine, label: "check_ap"}
	example_checks.pipeline_checks_for_views:check_join@{shape: subroutine, label: "check_join"}
	example_checks.pipeline_checks_for_views:check_bp@{shape: subroutine, label: "check_bp"}
	example_checks.pipeline_checks_for_views:AB@{shape: subroutine, label: "AB"}
	example_checks.pipeline_checks_for_views:check_ab@{shape: subroutine, label: "check_ab"}
	example_checks.pipeline_checks_for_views:print_result@{shape: subroutine, label: "print_result"}
	IO0@{shape: rect, label: "A"}
	IO1@{shape: rect, label: "D"}
	IO2@{shape: rect, label: "B"}

	class L0 node
	class L2,example_checks.pipeline_checks_for_views:check_a,example_checks.pipeline_checks_for_views:Ap,example_checks.pipeline_checks_for_views:Bp,example_checks.pipeline_checks_for_views:check_ap,example_checks.pipeline_checks_for_views:check_join,example_checks.pipeline_checks_for_views:check_bp,example_checks.pipeline_checks_for_views:AB,example_checks.pipeline_checks_for_views:check_ab,example_checks.pipeline_checks_for_views:print_result view
	class L00 io0
	class L01,IO0,IO1,IO2 io1
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
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running view 'check_a' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'Ap' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'Bp' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'check_ap' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'check_join' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'check_bp' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'AB' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'check_ab' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_checks_for_views'

```