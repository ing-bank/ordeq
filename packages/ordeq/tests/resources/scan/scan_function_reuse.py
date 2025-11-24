from pprint import pprint

import example_function_reuse
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_function_reuse))
print("Nodes:")
pprint(
    sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40
)
print("IOs:")
pprint(list(ios.values()), width=40)
