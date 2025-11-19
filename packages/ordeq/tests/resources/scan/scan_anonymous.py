from pprint import pprint

import example_anonymous
from ordeq._scan import scan

nodes, ios = scan(example_anonymous)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
