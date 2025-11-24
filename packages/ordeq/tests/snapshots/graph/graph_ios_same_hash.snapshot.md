## Resource

```python
# Resource showing that distinct IO objects with the same hash
# are modelled as distinct vertices in the graph.

import operator

from ordeq import Input, Node
from ordeq._graph import NodeIOGraph
from ordeq_common import Print


class Greeting(Input[str]):
    def __init__(self, value: str):
        self.value = value

    def load(self) -> str:
        return self.value

    def __hash__(self):
        return hash(self.value.lower())


x = Greeting("hello")
y = Greeting("HELLO")
assert hash(x) == hash(y)

graph = NodeIOGraph.from_nodes([
    Node(func=operator.eq, inputs=(x, y), outputs=(Print(),))
])
print("NodeIOGraph:")
print(graph)

```

## Output

```text
NodeIOGraph:
io-0 --> Node:Node(func=_operator:eq, inputs=[Input(id=ID1), Input(id=ID2)], outputs=[Print()])
io-1 --> Node:Node(func=_operator:eq, inputs=[Input(id=ID1), Input(id=ID2)], outputs=[Print()])
Node:Node(func=_operator:eq, inputs=[Input(id=ID1), Input(id=ID2)], outputs=[Print()]) --> io-2

```