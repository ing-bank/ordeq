from pprint import pprint

import example_nested
from ordeq._scan import scan

nodes, ios = scan(example_nested)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
