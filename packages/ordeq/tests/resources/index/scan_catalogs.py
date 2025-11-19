from pprint import pprint

import example_catalogs
from ordeq._index import index

nodes, ios = index(example_catalogs)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
