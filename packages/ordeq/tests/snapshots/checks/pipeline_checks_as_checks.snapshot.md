## Resource

```python
from ordeq import IO, node, run
from ordeq_common import Literal, StringBuffer
from ordeq_viz import viz

A = Literal("A")
B = Literal("B")
Ap = IO[str]()
Bp = IO[str]()
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


# Additional checks
D = Literal("D")


@node(inputs=[A, D], checks=[A])
def check_a(a: str, d: str) -> None:
    assert a != d, "A and D should not be equal"


@node(inputs=[Ap], checks=[Ap])
def check_ap(ap: str) -> None:
    assert ap.islower(), "Ap should be lowercase"


@node(inputs=[Bp], checks=[Bp])
def check_bp(bp: str) -> None:
    assert len(bp) == 3 * len("B"), "Bp should be three times the length of B"


@node(inputs=[Ap, Bp], checks=[Ap, Bp])
def check_join(ap: str, bp: str) -> None:
    assert len(ap) + len(bp) == 4


@node(inputs=[AB], checks=[AB])
def check_ab(ab: str) -> None:
    assert "a" in ab, "AB should contain 'a'"


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

	IO0 --> __main__:check_a
	IO1 --> __main__:check_a
	IO0 --> __main__:process_a
	__main__:process_a --> IO2
	IO3 --> __main__:process_b
	__main__:process_b --> IO4
	IO2 --> __main__:check_ap
	IO2 --> __main__:check_join
	IO4 --> __main__:check_join
	IO4 --> __main__:check_bp
	IO2 --> __main__:join
	IO4 --> __main__:join
	__main__:join --> IO5
	IO5 --> __main__:check_ab
	IO5 --> __main__:print_result

	__main__:check_a@{shape: subroutine, label: "check_a"}
	__main__:process_a@{shape: rounded, label: "process_a"}
	__main__:process_b@{shape: rounded, label: "process_b"}
	__main__:check_ap@{shape: subroutine, label: "check_ap"}
	__main__:check_join@{shape: subroutine, label: "check_join"}
	__main__:check_bp@{shape: subroutine, label: "check_bp"}
	__main__:join@{shape: rounded, label: "join"}
	__main__:check_ab@{shape: subroutine, label: "check_ab"}
	__main__:print_result@{shape: subroutine, label: "print_result"}
	IO2@{shape: rect, label: "Ap"}
	IO4@{shape: rect, label: "Bp"}
	IO5@{shape: rect, label: "AB"}
	IO0@{shape: rect, label: "A"}
	IO1@{shape: rect, label: "D"}
	IO3@{shape: rect, label: "B"}

	class L0,__main__:process_a,__main__:process_b,__main__:join node
	class L2,__main__:check_a,__main__:check_ap,__main__:check_join,__main__:check_bp,__main__:check_ab,__main__:print_result view
	class L00,IO2,IO4 io0
	class L01,IO0,IO1,IO3 io1
	class L02,IO5 io2
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
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading Literal('A')
INFO	ordeq.io	Loading Literal('D')
INFO	ordeq.runner	Running view "check_a" in module "__main__"
INFO	ordeq.runner	Running node "process_a" in module "__main__"
INFO	ordeq.io	Loading Literal('B')
INFO	ordeq.runner	Running node "process_b" in module "__main__"
INFO	ordeq.runner	Running view "check_ap" in module "__main__"
INFO	ordeq.runner	Running view "check_join" in module "__main__"
INFO	ordeq.runner	Running view "check_bp" in module "__main__"
INFO	ordeq.runner	Running node "join" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view "check_ab" in module "__main__"
INFO	ordeq.runner	Running view "print_result" in module "__main__"

```