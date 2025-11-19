from pprint import pprint

import example_imports
from ordeq._scan import scan

nodes, ios = scan(example_imports)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
