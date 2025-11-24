from pprint import pp

import ordeq_dev_tools
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(ordeq_dev_tools)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
