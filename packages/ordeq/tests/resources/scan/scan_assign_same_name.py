from pprint import pprint

import example_imports.assign_same_name
from ordeq._scan import scan

nodes, ios = scan(example_imports.assign_same_name)
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)
