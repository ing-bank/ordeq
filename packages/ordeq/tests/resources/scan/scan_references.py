from pprint import pprint

import example_references
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_references)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
