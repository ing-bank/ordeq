from pprint import pprint

import example_resources
from ordeq._scan import scan

nodes, ios = scan(example_resources)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
