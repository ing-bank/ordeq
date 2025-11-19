from pprint import pprint

import example_imports.local_import_made_global
from ordeq._index import index

nodes, ios = index(example_imports.local_import_made_global)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
