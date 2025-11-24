from pprint import pprint

import example_imports.assign_same_name
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.assign_same_name)
print("Nodes:")
pprint([node for node in sorted(nodes, key=lambda n: (nodes[n], n.ref))], width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
