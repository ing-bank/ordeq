from pprint import pp

import example_resources
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_resources)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
