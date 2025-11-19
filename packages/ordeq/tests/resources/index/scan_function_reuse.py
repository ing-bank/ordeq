from pprint import pprint

import example_function_reuse
from ordeq._index import index

nodes, ios = index(example_function_reuse)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
