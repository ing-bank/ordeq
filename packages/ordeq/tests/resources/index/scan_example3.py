from pprint import pprint

import example_3
from ordeq._index import index

nodes, ios = index(example_3)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
