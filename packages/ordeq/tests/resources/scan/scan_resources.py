from pprint import pprint

import example_resources
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_resources)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
