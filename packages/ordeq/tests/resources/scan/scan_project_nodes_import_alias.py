from pprint import pprint

import example_project.nodes_import_alias
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_import_alias)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
