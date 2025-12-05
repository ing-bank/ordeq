## Resource

```python
from example_checks import pipeline_checks_as_checks
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_checks_as_checks, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_checks_as_checks)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
		io_type_2@{shape: rect, label: "StringBuffer"}
	end

	example_checks.pipeline_checks_as_checks:A --> example_checks.pipeline_checks_as_checks:check_a
	example_checks.pipeline_checks_as_checks:D --> example_checks.pipeline_checks_as_checks:check_a
	example_checks.pipeline_checks_as_checks:B --> example_checks.pipeline_checks_as_checks:process_b
	example_checks.pipeline_checks_as_checks:process_b --> example_checks.pipeline_checks_as_checks:Bp
	example_checks.pipeline_checks_as_checks:A --> example_checks.pipeline_checks_as_checks:process_a
	example_checks.pipeline_checks_as_checks:process_a --> example_checks.pipeline_checks_as_checks:Ap
	example_checks.pipeline_checks_as_checks:Bp --> example_checks.pipeline_checks_as_checks:check_bp
	example_checks.pipeline_checks_as_checks:Ap --> example_checks.pipeline_checks_as_checks:check_join
	example_checks.pipeline_checks_as_checks:Bp --> example_checks.pipeline_checks_as_checks:check_join
	example_checks.pipeline_checks_as_checks:Ap --> example_checks.pipeline_checks_as_checks:check_ap
	example_checks.pipeline_checks_as_checks:Ap --> example_checks.pipeline_checks_as_checks:join
	example_checks.pipeline_checks_as_checks:Bp --> example_checks.pipeline_checks_as_checks:join
	example_checks.pipeline_checks_as_checks:join --> example_checks.pipeline_checks_as_checks:AB
	example_checks.pipeline_checks_as_checks:AB --> example_checks.pipeline_checks_as_checks:check_ab
	example_checks.pipeline_checks_as_checks:AB --> example_checks.pipeline_checks_as_checks:print_result

	example_checks.pipeline_checks_as_checks:check_a@{shape: subroutine, label: "check_a"}
	example_checks.pipeline_checks_as_checks:process_b@{shape: rounded, label: "process_b"}
	example_checks.pipeline_checks_as_checks:process_a@{shape: rounded, label: "process_a"}
	example_checks.pipeline_checks_as_checks:check_bp@{shape: subroutine, label: "check_bp"}
	example_checks.pipeline_checks_as_checks:check_join@{shape: subroutine, label: "check_join"}
	example_checks.pipeline_checks_as_checks:check_ap@{shape: subroutine, label: "check_ap"}
	example_checks.pipeline_checks_as_checks:join@{shape: rounded, label: "join"}
	example_checks.pipeline_checks_as_checks:check_ab@{shape: subroutine, label: "check_ab"}
	example_checks.pipeline_checks_as_checks:print_result@{shape: subroutine, label: "print_result"}
	example_checks.pipeline_checks_as_checks:AB@{shape: rect, label: "AB"}
	example_checks.pipeline_checks_as_checks:Ap@{shape: rect, label: "Ap"}
	example_checks.pipeline_checks_as_checks:Bp@{shape: rect, label: "Bp"}
	example_checks.pipeline_checks_as_checks:A@{shape: rect, label: "A"}
	example_checks.pipeline_checks_as_checks:B@{shape: rect, label: "B"}
	example_checks.pipeline_checks_as_checks:D@{shape: rect, label: "D"}

	class node_type,example_checks.pipeline_checks_as_checks:process_b,example_checks.pipeline_checks_as_checks:process_a,example_checks.pipeline_checks_as_checks:join node
	class view_type,example_checks.pipeline_checks_as_checks:check_a,example_checks.pipeline_checks_as_checks:check_bp,example_checks.pipeline_checks_as_checks:check_join,example_checks.pipeline_checks_as_checks:check_ap,example_checks.pipeline_checks_as_checks:check_ab,example_checks.pipeline_checks_as_checks:print_result view
	class io_type_0,example_checks.pipeline_checks_as_checks:Ap,example_checks.pipeline_checks_as_checks:Bp io0
	class io_type_1,example_checks.pipeline_checks_as_checks:A,example_checks.pipeline_checks_as_checks:B,example_checks.pipeline_checks_as_checks:D io1
	class io_type_2,example_checks.pipeline_checks_as_checks:AB io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb

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
DEBUG	ordeq.io	Loading cached data for Input 'A' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for Input 'D' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'check_a' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for Input 'B' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running node 'process_b' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO 'Bp' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for Input 'A' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running node 'process_a' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO 'Ap' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for IO 'Bp' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'check_bp' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO 'Ap' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for IO 'Bp' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'check_join' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
DEBUG	ordeq.io	Loading cached data for IO 'Ap' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'check_ap' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID7)
DEBUG	ordeq.io	Loading cached data for IO 'Ap' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for IO 'Bp' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running node 'join' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.io	Saving StringBuffer 'AB' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for StringBuffer 'AB' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'AB' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'check_ab' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID8)
DEBUG	ordeq.io	Loading cached data for StringBuffer 'AB' in module 'example_checks.pipeline_checks_as_checks'
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Persisting data for IO(id=ID9)
DEBUG	ordeq.io	Unpersisting data for IO 'Ap' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Unpersisting data for IO 'Bp' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'AB' in module 'example_checks.pipeline_checks_as_checks'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID9)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID7)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID8)

```