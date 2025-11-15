## Resource

```python
# Resource showing that equivalent IO instances are modelled as distinct
# vertices in the graph.
from pprint import pprint

from ordeq import Input, Node
from ordeq._graph import NodeIOGraph
from ordeq_common import Print
import operator


class Greeting(Input[str]):
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other):
        return self.value.lower() == self.value.lower()

    def __hash__(self):
        return hash(self.value.lower())

    def load(self) -> str:
        return self.value


x = Greeting("hello")
y = Greeting("HELLO")
assert hash(x) == hash(y)
assert x == y

graph = NodeIOGraph.from_nodes([
    Node(func=operator.eq, inputs=(x, y), outputs=(Print(),), name="are_greetings_equal")
])
print("NodeIOGraph:")
print(graph)

```

## Output

```text
NodeIOGraph:
io-0 --> Node:are_greetings_equal
io-1 --> Node:are_greetings_equal
Node:are_greetings_equal --> io-2

```