from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._scan import scan

nodes, ios = scan(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)
