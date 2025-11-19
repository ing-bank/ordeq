from pprint import pprint

import example_nested
from ordeq._scan import scan

nodes, ios = scan(example_nested)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
