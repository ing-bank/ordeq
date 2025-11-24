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
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Literal"}
		L02@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_checks.pipeline_checks_as_checks:check_a
	IO1 --> example_checks.pipeline_checks_as_checks:check_a
	IO0 --> example_checks.pipeline_checks_as_checks:process_a
	example_checks.pipeline_checks_as_checks:process_a --> IO2
	IO3 --> example_checks.pipeline_checks_as_checks:process_b
	example_checks.pipeline_checks_as_checks:process_b --> IO4
	IO2 --> example_checks.pipeline_checks_as_checks:check_ap
	IO2 --> example_checks.pipeline_checks_as_checks:check_join
	IO4 --> example_checks.pipeline_checks_as_checks:check_join
	IO4 --> example_checks.pipeline_checks_as_checks:check_bp
	IO2 --> example_checks.pipeline_checks_as_checks:join
	IO4 --> example_checks.pipeline_checks_as_checks:join
	example_checks.pipeline_checks_as_checks:join --> IO5
	IO5 --> example_checks.pipeline_checks_as_checks:check_ab
	IO5 --> example_checks.pipeline_checks_as_checks:print_result

	example_checks.pipeline_checks_as_checks:check_a@{shape: subroutine, label: "check_a"}
	example_checks.pipeline_checks_as_checks:process_a@{shape: rounded, label: "process_a"}
	example_checks.pipeline_checks_as_checks:process_b@{shape: rounded, label: "process_b"}
	example_checks.pipeline_checks_as_checks:check_ap@{shape: subroutine, label: "check_ap"}
	example_checks.pipeline_checks_as_checks:check_join@{shape: subroutine, label: "check_join"}
	example_checks.pipeline_checks_as_checks:check_bp@{shape: subroutine, label: "check_bp"}
	example_checks.pipeline_checks_as_checks:join@{shape: rounded, label: "join"}
	example_checks.pipeline_checks_as_checks:check_ab@{shape: subroutine, label: "check_ab"}
	example_checks.pipeline_checks_as_checks:print_result@{shape: subroutine, label: "print_result"}
	IO2@{shape: rect, label: "Ap"}
	IO4@{shape: rect, label: "Bp"}
	IO5@{shape: rect, label: "AB"}
	IO0@{shape: rect, label: "A"}
	IO1@{shape: rect, label: "D"}
	IO3@{shape: rect, label: "B"}

	class L0,example_checks.pipeline_checks_as_checks:process_a,example_checks.pipeline_checks_as_checks:process_b,example_checks.pipeline_checks_as_checks:join node
	class L2,example_checks.pipeline_checks_as_checks:check_a,example_checks.pipeline_checks_as_checks:check_ap,example_checks.pipeline_checks_as_checks:check_join,example_checks.pipeline_checks_as_checks:check_bp,example_checks.pipeline_checks_as_checks:check_ab,example_checks.pipeline_checks_as_checks:print_result view
	class L00,IO2,IO4 io0
	class L01,IO0,IO1,IO3 io1
	class L02,IO5 io2
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
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('A')
INFO	ordeq.io	Loading Literal('D')
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:check_a'
INFO	ordeq.runner	Running node 'example_checks.pipeline_checks_as_checks:process_a'
INFO	ordeq.io	Loading Literal('B')
INFO	ordeq.runner	Running node 'example_checks.pipeline_checks_as_checks:process_b'
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:check_ap'
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:check_join'
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:check_bp'
INFO	ordeq.runner	Running node 'example_checks.pipeline_checks_as_checks:join'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:check_ab'
INFO	ordeq.runner	Running view 'example_checks.pipeline_checks_as_checks:print_result'

```