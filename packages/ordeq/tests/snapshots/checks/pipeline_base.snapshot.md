## Resource

```python
from example_checks import pipeline_base
from ordeq import run
from ordeq_viz import viz

if __name__ == "__main__":
    print(viz(pipeline_base, fmt="mermaid"))

    print("Expected output is 'aBBB'")
    run(pipeline_base)

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

	example_checks.pipeline_base:A --> example_checks.pipeline_base:process_a
	example_checks.pipeline_base:process_a --> example_checks.pipeline_base:Ap
	example_checks.pipeline_base:B --> example_checks.pipeline_base:process_b
	example_checks.pipeline_base:process_b --> example_checks.pipeline_base:Bp
	example_checks.pipeline_base:Ap --> example_checks.pipeline_base:join
	example_checks.pipeline_base:Bp --> example_checks.pipeline_base:join
	example_checks.pipeline_base:join --> example_checks.pipeline_base:AB
	example_checks.pipeline_base:AB --> example_checks.pipeline_base:print_result

	example_checks.pipeline_base:process_a@{shape: rounded, label: "process_a"}
	example_checks.pipeline_base:process_b@{shape: rounded, label: "process_b"}
	example_checks.pipeline_base:join@{shape: rounded, label: "join"}
	example_checks.pipeline_base:print_result@{shape: subroutine, label: "print_result"}
	example_checks.pipeline_base:AB@{shape: rect, label: "AB"}
	example_checks.pipeline_base:Ap@{shape: rect, label: "Ap"}
	example_checks.pipeline_base:Bp@{shape: rect, label: "Bp"}
	example_checks.pipeline_base:A@{shape: rect, label: "A"}
	example_checks.pipeline_base:B@{shape: rect, label: "B"}

	class node_type,example_checks.pipeline_base:process_a,example_checks.pipeline_base:process_b,example_checks.pipeline_base:join node
	class view_type,example_checks.pipeline_base:print_result view
	class io_type_0,example_checks.pipeline_base:Ap,example_checks.pipeline_base:Bp io0
	class io_type_1,example_checks.pipeline_base:A,example_checks.pipeline_base:B io1
	class io_type_2,example_checks.pipeline_base:AB io2
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
DEBUG	ordeq.io	Loading cached data for Input 'A' in module 'example_checks.pipeline_base'
INFO	ordeq.runner	Running node 'process_a' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Persisting data for IO 'Ap' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Loading cached data for Input 'B' in module 'example_checks.pipeline_base'
INFO	ordeq.runner	Running node 'process_b' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Persisting data for IO 'Bp' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Loading cached data for IO 'Ap' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Loading cached data for IO 'Bp' in module 'example_checks.pipeline_base'
INFO	ordeq.runner	Running node 'join' in module 'example_checks.pipeline_base'
INFO	ordeq.io	Saving StringBuffer 'AB' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Persisting data for StringBuffer 'AB' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'AB' in module 'example_checks.pipeline_base'
INFO	ordeq.runner	Running view 'print_result' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO 'Bp' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Unpersisting data for IO 'Ap' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'AB' in module 'example_checks.pipeline_base'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```