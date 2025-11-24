from pprint import pprint

import example_imports.aliased_catalog
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.aliased_catalog)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
