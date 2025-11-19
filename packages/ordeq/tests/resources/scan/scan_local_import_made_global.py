from pprint import pprint

import example_imports.local_import_made_global
from ordeq._scan import scan

nodes, ios = scan(example_imports.local_import_made_global)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
