from pprint import pprint

import example_imports.assign_same_name
from ordeq._scan import scan

nodes, ios = scan(example_imports.assign_same_name)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
