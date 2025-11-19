from pprint import pprint

import example_imports.local_import
from ordeq._index import index

nodes, ios = index(example_imports.local_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
