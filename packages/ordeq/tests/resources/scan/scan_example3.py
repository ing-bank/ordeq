from pprint import pp

import example_3
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_3)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
