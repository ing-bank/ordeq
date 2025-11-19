from pprint import pprint

import example_3
from ordeq._scan import scan

nodes, ios = scan(example_3)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
