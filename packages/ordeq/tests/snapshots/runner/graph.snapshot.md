## Resource

```python
from ordeq import node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")
R1 = StringBuffer()
R2 = StringBuffer()
R3 = StringBuffer()
R4 = StringBuffer()


@node(inputs=[I1, I2], outputs=[R1])
def f1(i: str, j: str) -> str:
    return f"{i} + {j}"


@node(inputs=[I2, R1], outputs=[R2])
def f2(i: str, j: str) -> str:
    return f"{i} - {j}"


@node(inputs=[R1], outputs=[R3])
def f3(i: str) -> str:
    return f"{i} * 2"


@node(inputs=[R1, R2, R3], outputs=[R4])
def f4(i: str, j: str, k: str) -> str:
    return f"{i} / {j} + {k}"


pipeline = [f1, f2, f3, f4]

run(*pipeline, save="all", verbose=True)
print(R4.load())

run(*pipeline, save="sinks", verbose=True)
print(R4.load())

run(*pipeline, save="none", verbose=True)
print(R4.load())

```

## Output

```text
NodeResourceGraph(nodes=4, resources=6, edges={Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH3>))], Node(name=__main__:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH4>))], Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH5>))], Node(name=__main__:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH5>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH6>))], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH3>)): [Node(name=__main__:f3, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH5>)]), Node(name=__main__:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH5>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH4>)): [Node(name=__main__:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH5>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH5>)): [Node(name=__main__:f4, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>), StringBuffer(_buffer=<_io.StringIO object at HASH5>), StringBuffer(_buffer=<_io.StringIO object at HASH4>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH6>)): []})
Hello + world! / world! - Hello + world! + Hello + world! * 2
NodeResourceGraph(nodes=4, resources=6, edges={Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID1)]): [Resource(value=IO(id=ID1))], Node(name=__main__:f3, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]): [Resource(value=IO(id=ID2))], Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID1)], outputs=[IO(id=ID3)]): [Resource(value=IO(id=ID3))], Node(name=__main__:f4, inputs=[IO(id=ID1), IO(id=ID3), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)]): [Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH6>))], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID1)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID1)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID1)], outputs=[IO(id=ID3)])], Resource(value=IO(id=ID1)): [Node(name=__main__:f3, inputs=[IO(id=ID1)], outputs=[IO(id=ID2)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID1)], outputs=[IO(id=ID3)]), Node(name=__main__:f4, inputs=[IO(id=ID1), IO(id=ID3), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=IO(id=ID2)): [Node(name=__main__:f4, inputs=[IO(id=ID1), IO(id=ID3), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=IO(id=ID3)): [Node(name=__main__:f4, inputs=[IO(id=ID1), IO(id=ID3), IO(id=ID2)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH6>)): []})
Hello + world! / world! - Hello + world! + Hello + world! * 2Hello + world! / world! - Hello + world! + Hello + world! * 2
NodeResourceGraph(nodes=4, resources=6, edges={Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID4)]): [Resource(value=IO(id=ID4))], Node(name=__main__:f3, inputs=[IO(id=ID4)], outputs=[IO(id=ID5)]): [Resource(value=IO(id=ID5))], Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID4)], outputs=[IO(id=ID3)]): [Resource(value=IO(id=ID3))], Node(name=__main__:f4, inputs=[IO(id=ID4), IO(id=ID3), IO(id=ID5)], outputs=[IO(id=ID6)]): [Resource(value=IO(id=ID6))], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID4)])], Resource(value=StringBuffer(_buffer=<_io.StringIO object at HASH2>)): [Node(name=__main__:f1, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[IO(id=ID4)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID4)], outputs=[IO(id=ID3)])], Resource(value=IO(id=ID4)): [Node(name=__main__:f3, inputs=[IO(id=ID4)], outputs=[IO(id=ID5)]), Node(name=__main__:f2, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>), IO(id=ID4)], outputs=[IO(id=ID3)]), Node(name=__main__:f4, inputs=[IO(id=ID4), IO(id=ID3), IO(id=ID5)], outputs=[IO(id=ID6)])], Resource(value=IO(id=ID5)): [Node(name=__main__:f4, inputs=[IO(id=ID4), IO(id=ID3), IO(id=ID5)], outputs=[IO(id=ID6)])], Resource(value=IO(id=ID3)): [Node(name=__main__:f4, inputs=[IO(id=ID4), IO(id=ID3), IO(id=ID5)], outputs=[IO(id=ID6)])], Resource(value=IO(id=ID6)): []})
Hello + world! / world! - Hello + world! + Hello + world! * 2Hello + world! / world! - Hello + world! + Hello + world! * 2

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node "f1" in module "__main__"
INFO	ordeq.runner	Running node "f2" in module "__main__"
INFO	ordeq.runner	Running node "f3" in module "__main__"
INFO	ordeq.runner	Running node "f4" in module "__main__"
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH6>)

```