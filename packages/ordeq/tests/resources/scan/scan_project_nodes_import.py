from pprint import pp

import example_project.nodes_import
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_import)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
