from pprint import pprint

import example_project.nodes_import
from ordeq._index import index

nodes, ios = index(example_project.nodes_import)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
