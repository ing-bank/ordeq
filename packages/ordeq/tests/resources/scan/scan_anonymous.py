from pprint import pprint

import example_anonymous
from ordeq._scan import scan

nodes, ios = scan(example_anonymous)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
