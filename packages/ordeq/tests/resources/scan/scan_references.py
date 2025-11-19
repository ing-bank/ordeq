from pprint import pprint

import example_references
from ordeq._scan import scan

nodes, ios = scan(example_references)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
