from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(ordeq_dev_tools))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
