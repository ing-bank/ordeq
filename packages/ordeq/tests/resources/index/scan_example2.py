from pprint import pprint

import example_2
from ordeq._index import index

nodes, ios = index(example_2)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
