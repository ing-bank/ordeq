from pprint import pprint

import example_project.nodes_import
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_import)
print("Nodes:")
pprint(nodes, width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
