from pprint import pprint

import example_1
from ordeq._index import index

nodes, ios = index(example_1)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
