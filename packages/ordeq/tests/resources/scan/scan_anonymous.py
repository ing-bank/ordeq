from pprint import pprint

import example_anonymous
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_anonymous)
print("Nodes:")
pprint(
    sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40
)
print("IOs:")
pprint(list(ios.values()), width=40)
