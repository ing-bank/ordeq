from pprint import pprint

import example_anonymous
from ordeq._index import index

nodes, ios = index(example_anonymous)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
