from pprint import pprint

import ordeq_dev_tools
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(ordeq_dev_tools)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
