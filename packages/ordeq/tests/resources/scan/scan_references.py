from pprint import pp

import example_references
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_references)
print("Nodes:")
pp(nodes, width=40)
print("IOs:")
pp(list(ios.values()), width=40)
