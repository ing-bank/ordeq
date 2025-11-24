from pprint import pp

import example_anonymous
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_anonymous)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
