from pprint import pprint

import example_project.nodes_import_alias
from ordeq._index import index

nodes, ios = index(example_project.nodes_import_alias)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
