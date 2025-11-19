from pprint import pprint

import example_references
from ordeq._index import index

nodes, ios = index(example_references)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
