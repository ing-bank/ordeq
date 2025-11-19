from pprint import pprint

import example_imports.assign_same_name
from ordeq._scan import scan

nodes, ios = scan(example_imports.assign_same_name)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
