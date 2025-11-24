from pprint import pprint

import example_references
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_references)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
