from pprint import pprint

import example_1
from ordeq._scan import scan

nodes, ios = scan(example_1)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
