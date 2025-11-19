from pprint import pprint

import example_rag_pipeline
from ordeq._index import index

nodes, ios = index(example_rag_pipeline)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
