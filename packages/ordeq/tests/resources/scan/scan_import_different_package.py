from pprint import pprint

import example_imports.import_different_package
from ordeq._scan import scan

nodes, ios = scan(example_imports.import_different_package)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
