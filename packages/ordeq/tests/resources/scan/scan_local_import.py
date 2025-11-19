from pprint import pprint

import example_imports.local_import
from ordeq._scan import scan

nodes, ios = scan(example_imports.local_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
