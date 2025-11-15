## Resource

```python
# Resource showing that equivalent IO instances are modelled as distinct
# vertices in the graph.

import operator

from ordeq import Input, Node
from ordeq._graph import NodeIOGraph
from ordeq_common import Print


class Greeting(Input[str]):
    def __init__(self, value: str):
        self.value = value

    def load(self, show: bool = False) -> str:
        if show:
            print('Loading greeting', self.value)
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


x = Greeting("hello")
y = x.with_load_options(
    show=True
)
assert hash(x) == hash(y)
assert x == y

graph = NodeIOGraph.from_nodes([
    Node(
        func=operator.eq,
        inputs=(x, y),
        outputs=(Print(),),
        name="are_greetings_equal",
    )
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