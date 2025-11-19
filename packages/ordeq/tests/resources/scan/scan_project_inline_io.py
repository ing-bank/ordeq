from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()), width=40)
