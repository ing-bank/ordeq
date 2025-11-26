from pprint import pp

import example_nested
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_nested)
print("Nodes:")
print(nodes)
print("IOs:")
pp(list(ios.values()), width=40)
