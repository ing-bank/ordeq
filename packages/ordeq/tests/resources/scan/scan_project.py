from pprint import pprint

import example_project
from ordeq._scan import scan

nodes, ios = scan(example_project)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
