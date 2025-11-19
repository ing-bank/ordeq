from pprint import pprint

import example_imports.aliased_catalog
from ordeq._index import index

nodes, ios = index(example_imports.aliased_catalog)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
