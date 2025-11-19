from pprint import pprint

import example_imports
from ordeq._scan import scan

nodes, ios = scan(example_imports)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
