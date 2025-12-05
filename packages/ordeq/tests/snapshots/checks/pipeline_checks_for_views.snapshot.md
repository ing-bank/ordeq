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
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
	end

	example_checks.pipeline_checks_for_views:A --> example_checks.pipeline_checks_for_views:check_a
	example_checks.pipeline_checks_for_views:D --> example_checks.pipeline_checks_for_views:check_a
	example_checks.pipeline_checks_for_views:A --> example_checks.pipeline_checks_for_views:Ap
	example_checks.pipeline_checks_for_views:B --> example_checks.pipeline_checks_for_views:Bp
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
	example_checks.pipeline_checks_for_views:A@{shape: rect, label: "A"}
	example_checks.pipeline_checks_for_views:B@{shape: rect, label: "B"}
	example_checks.pipeline_checks_for_views:D@{shape: rect, label: "D"}

	class view_type,example_checks.pipeline_checks_for_views:check_a,example_checks.pipeline_checks_for_views:Ap,example_checks.pipeline_checks_for_views:Bp,example_checks.pipeline_checks_for_views:check_ap,example_checks.pipeline_checks_for_views:check_join,example_checks.pipeline_checks_for_views:check_bp,example_checks.pipeline_checks_for_views:AB,example_checks.pipeline_checks_for_views:check_ab,example_checks.pipeline_checks_for_views:print_result view
	class io_type_0 io0
	class io_type_1,example_checks.pipeline_checks_for_views:A,example_checks.pipeline_checks_for_views:B,example_checks.pipeline_checks_for_views:D io1
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

Expected output is 'aBBB'
aBBB

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Loading Input 'A' in module 'example_checks.pipeline_checks_for_views'
DEBUG	ordeq.io	Loading cached data for Input 'A' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Loading Input 'D' in module 'example_checks.pipeline_checks_for_views'
DEBUG	ordeq.io	Loading cached data for Input 'D' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'check_a' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID4)
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
INFO	ordeq.runner	Loading Input 'A' in module 'example_checks.pipeline_checks_for_views'
DEBUG	ordeq.io	Loading cached data for Input 'A' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'Ap' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID5)
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
INFO	ordeq.runner	Loading Input 'B' in module 'example_checks.pipeline_checks_for_views'
DEBUG	ordeq.io	Loading cached data for Input 'B' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Running view 'Bp' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID6)
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
INFO	ordeq.runner	Loading IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
INFO	ordeq.runner	Running view 'check_ap' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID7)
DEBUG	ordeq.io	Persisting data for IO(id=ID7)
INFO	ordeq.runner	Loading IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
INFO	ordeq.runner	Loading IO(id=ID6)
DEBUG	ordeq.io	Loading cached data for IO(id=ID6)
INFO	ordeq.runner	Running view 'check_join' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID8)
DEBUG	ordeq.io	Persisting data for IO(id=ID8)
INFO	ordeq.runner	Loading IO(id=ID6)
DEBUG	ordeq.io	Loading cached data for IO(id=ID6)
INFO	ordeq.runner	Running view 'check_bp' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID9)
DEBUG	ordeq.io	Persisting data for IO(id=ID9)
INFO	ordeq.runner	Loading IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
INFO	ordeq.runner	Loading IO(id=ID6)
DEBUG	ordeq.io	Loading cached data for IO(id=ID6)
INFO	ordeq.runner	Running view 'AB' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID10)
DEBUG	ordeq.io	Persisting data for IO(id=ID10)
INFO	ordeq.runner	Loading IO(id=ID10)
DEBUG	ordeq.io	Loading cached data for IO(id=ID10)
INFO	ordeq.runner	Running view 'check_ab' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID11)
DEBUG	ordeq.io	Persisting data for IO(id=ID11)
INFO	ordeq.runner	Loading IO(id=ID10)
DEBUG	ordeq.io	Loading cached data for IO(id=ID10)
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_checks_for_views'
INFO	ordeq.runner	Saving IO(id=ID12)
DEBUG	ordeq.io	Persisting data for IO(id=ID12)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID9)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID8)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID7)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID10)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID11)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID12)

```