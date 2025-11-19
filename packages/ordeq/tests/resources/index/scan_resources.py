from pprint import pprint

import example_resources
from ordeq._index import index

nodes, ios = index(example_resources)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
