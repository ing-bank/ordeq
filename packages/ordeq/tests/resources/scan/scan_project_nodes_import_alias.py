from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)
