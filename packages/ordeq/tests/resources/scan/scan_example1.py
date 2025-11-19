from pprint import pprint

import example_1
from ordeq._scan import scan

nodes, ios = scan(example_1)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
