from pprint import pprint

import example_nested
from ordeq._index import index

nodes, ios = index(example_nested)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
