from pprint import pprint

import example_2
from ordeq._scan import scan

nodes, ios = scan(example_2)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
