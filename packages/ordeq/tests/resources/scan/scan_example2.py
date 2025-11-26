from pprint import pp

import example_2
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_2)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
