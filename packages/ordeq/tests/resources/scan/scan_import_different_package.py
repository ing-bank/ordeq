from pprint import pprint

import example_imports.import_different_package
from ordeq._scan import scan

nodes, ios = scan(example_imports.import_different_package)
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)
