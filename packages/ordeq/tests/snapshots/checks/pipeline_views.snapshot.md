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
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
	end

	example_checks.pipeline_views:A --> example_checks.pipeline_views:Ap
	example_checks.pipeline_views:B --> example_checks.pipeline_views:Bp
	example_checks.pipeline_views:Ap --> example_checks.pipeline_views:AB
	example_checks.pipeline_views:Bp --> example_checks.pipeline_views:AB
	example_checks.pipeline_views:AB --> example_checks.pipeline_views:print_result

	example_checks.pipeline_views:Ap@{shape: subroutine, label: "Ap"}
	example_checks.pipeline_views:Bp@{shape: subroutine, label: "Bp"}
	example_checks.pipeline_views:AB@{shape: subroutine, label: "AB"}
	example_checks.pipeline_views:print_result@{shape: subroutine, label: "print_result"}
	example_checks.pipeline_views:A@{shape: rect, label: "A"}
	example_checks.pipeline_views:B@{shape: rect, label: "B"}

	class node_type node
	class view_type,example_checks.pipeline_views:Ap,example_checks.pipeline_views:Bp,example_checks.pipeline_views:AB,example_checks.pipeline_views:print_result view
	class io_type_0 io0
	class io_type_1,example_checks.pipeline_views:A,example_checks.pipeline_views:B io1
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
DEBUG	ordeq.io	Loading cached data for 'A' in module 'example_checks.pipeline_views'
INFO	ordeq.runner	Running view 'Ap' in module 'example_checks.pipeline_views'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for 'B' in module 'example_checks.pipeline_views'
INFO	ordeq.runner	Running view 'Bp' in module 'example_checks.pipeline_views'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)
INFO	ordeq.runner	Running view 'AB' in module 'example_checks.pipeline_views'
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_views'
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID6)

```