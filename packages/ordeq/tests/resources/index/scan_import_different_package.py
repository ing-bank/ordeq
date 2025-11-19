from pprint import pprint

import example_imports.import_different_package
from ordeq._index import index

nodes, ios = index(example_imports.import_different_package)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
