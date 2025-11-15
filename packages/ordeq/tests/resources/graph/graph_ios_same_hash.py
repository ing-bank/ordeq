# Resource showing that distinct IO objects with the same hash
# are modelled as distinct vertices in the graph.

from ordeq import Input, Node
from ordeq._graph import NodeIOGraph
from ordeq_common import Print
import operator


class Greeting(Input[str]):
    def __init__(self, value: str):
        self.value = value

    def __hash__(self):
        return hash(self.value.lower())

    def load(self) -> str:
        return self.value


x = Greeting("hello")
y = Greeting("HELLO")
assert hash(x) == hash(y)

graph = NodeIOGraph.from_nodes([
    Node(func=operator.eq, inputs=(x, y), outputs=(Print(),), name="are_greetings_equal")
])
print("NodeIOGraph:")
print(graph)
