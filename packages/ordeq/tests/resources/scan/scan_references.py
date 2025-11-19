from pprint import pprint

import example_references
from ordeq._scan import scan

nodes, ios = scan(example_references)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
