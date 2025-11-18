## Resource

```python
from ordeq import IO, node, run
from ordeq_common import Literal, StringBuffer
from ordeq_viz import viz

A = Literal("A")
B = Literal("B")
Ap = IO()
Bp = IO()
AB = StringBuffer()


@node(inputs=A, outputs=Ap)
def process_a(data: str) -> str:
    return data.lower()


@node(inputs=B, outputs=Bp)
def process_b(data: str) -> str:
    return data * 3


@node(inputs=[Ap, Bp], outputs=AB)
def join(a: str, b: str) -> str:
    return a + b


@node(inputs=AB)
def print_result(data: str) -> None:
    print(data)


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)

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

	IO0 --> __main__:join
	IO1 --> __main__:join
	__main__:join --> IO2
	IO2 --> __main__:print_result
	IO3 --> __main__:process_a
	__main__:process_a --> IO0
	IO4 --> __main__:process_b
	__main__:process_b --> IO1

	__main__:join@{shape: rounded, label: "join"}
	__main__:print_result@{shape: subroutine, label: "print_result"}
	__main__:process_a@{shape: rounded, label: "process_a"}
	__main__:process_b@{shape: rounded, label: "process_b"}
	IO0@{shape: rect, label: "Ap"}
	IO1@{shape: rect, label: "Bp"}
	IO2@{shape: rect, label: "AB"}
	IO3@{shape: rect, label: "A"}
	IO4@{shape: rect, label: "B"}

	class L0,__main__:join,__main__:process_a,__main__:process_b node
	class L2,__main__:print_result view
	class L00,IO0,IO1 io0
	class L01,IO3,IO4 io1
	class L02,IO2 io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb

aBBB

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:print_result'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('A')
INFO	ordeq.runner	Running node "process_a" in module "__main__"
INFO	ordeq.io	Loading Literal('B')
INFO	ordeq.runner	Running node "process_b" in module "__main__"
INFO	ordeq.runner	Running node "join" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "print_result" in module "__main__"

```