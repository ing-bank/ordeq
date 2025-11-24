from pprint import pprint

import example_imports.local_import_made_global
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_imports.local_import_made_global)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: n.ref), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)
