from pprint import pprint

import example_project
from ordeq._index import index

nodes, ios = index(example_project)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
