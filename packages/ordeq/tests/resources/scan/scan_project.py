from pprint import pprint

import example_project
from ordeq._scan import scan

nodes, ios = scan(example_project)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)
