from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
