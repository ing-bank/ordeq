from pprint import pprint

import example_project.nodes_with_inline_io
from ordeq._index import index

nodes, ios = index(example_project.nodes_with_inline_io)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
