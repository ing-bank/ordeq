from pprint import pprint

import example_empty
from ordeq._index import index

nodes, ios = index(example_empty)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
