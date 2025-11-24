## Resource

```python
from example_checks import pipeline_checks_as_nodes
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_checks_as_nodes, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_checks_as_nodes)

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
		L02@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_checks.pipeline_checks_as_nodes:process_a
	example_checks.pipeline_checks_as_nodes:process_a --> IO1
	IO2 --> example_checks.pipeline_checks_as_nodes:process_b
	example_checks.pipeline_checks_as_nodes:process_b --> IO3
	IO1 --> example_checks.pipeline_checks_as_nodes:join
	IO3 --> example_checks.pipeline_checks_as_nodes:join
	example_checks.pipeline_checks_as_nodes:join --> IO4
	IO0 --> example_checks.pipeline_checks_as_nodes:check_a
	IO5 --> example_checks.pipeline_checks_as_nodes:check_a
	IO4 --> example_checks.pipeline_checks_as_nodes:check_ab
	IO4 --> example_checks.pipeline_checks_as_nodes:print_result
	IO1 --> example_checks.pipeline_checks_as_nodes:check_ap
	IO1 --> example_checks.pipeline_checks_as_nodes:check_join
	IO3 --> example_checks.pipeline_checks_as_nodes:check_join
	IO3 --> example_checks.pipeline_checks_as_nodes:check_bp

	example_checks.pipeline_checks_as_nodes:process_a@{shape: rounded, label: "process_a"}
	example_checks.pipeline_checks_as_nodes:process_b@{shape: rounded, label: "process_b"}
	example_checks.pipeline_checks_as_nodes:join@{shape: rounded, label: "join"}
	example_checks.pipeline_checks_as_nodes:check_a@{shape: subroutine, label: "check_a"}
	example_checks.pipeline_checks_as_nodes:check_ab@{shape: subroutine, label: "check_ab"}
	example_checks.pipeline_checks_as_nodes:print_result@{shape: subroutine, label: "print_result"}
	example_checks.pipeline_checks_as_nodes:check_ap@{shape: subroutine, label: "check_ap"}
	example_checks.pipeline_checks_as_nodes:check_join@{shape: subroutine, label: "check_join"}
	example_checks.pipeline_checks_as_nodes:check_bp@{shape: subroutine, label: "check_bp"}
	IO1@{shape: rect, label: "Ap"}
	IO3@{shape: rect, label: "Bp"}
	IO4@{shape: rect, label: "AB"}
	IO0@{shape: rect, label: "A"}
	IO2@{shape: rect, label: "B"}
	IO5@{shape: rect, label: "D"}

	class L0,example_checks.pipeline_checks_as_nodes:process_a,example_checks.pipeline_checks_as_nodes:process_b,example_checks.pipeline_checks_as_nodes:join node
	class L2,example_checks.pipeline_checks_as_nodes:check_a,example_checks.pipeline_checks_as_nodes:check_ab,example_checks.pipeline_checks_as_nodes:print_result,example_checks.pipeline_checks_as_nodes:check_ap,example_checks.pipeline_checks_as_nodes:check_join,example_checks.pipeline_checks_as_nodes:check_bp view
	class L00,IO1,IO3 io0
	class L01,IO0,IO2,IO5 io1
	class L02,IO4 io2
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
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running node 'process_a' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for Input(id=ID2)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
INFO	ordeq.runner	Running node 'process_b' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
INFO	ordeq.runner	Running node 'join' in module 'example_checks.pipeline_checks_as_nodes'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
INFO	ordeq.runner	Running view 'check_a' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view 'check_ab' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID7)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID8)
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
INFO	ordeq.runner	Running view 'check_ap' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID9)
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
INFO	ordeq.runner	Running view 'check_join' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID10)
DEBUG	ordeq.io	Loading cached data for IO(id=ID5)
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
INFO	ordeq.runner	Running view 'check_bp' in module 'example_checks.pipeline_checks_as_nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID11)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID7)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID10)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID11)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID9)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID8)

```