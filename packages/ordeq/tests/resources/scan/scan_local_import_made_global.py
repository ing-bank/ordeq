from pprint import pprint

import example_imports.local_import_made_global
from ordeq._scan import scan

nodes, ios = scan(example_imports.local_import_made_global)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
