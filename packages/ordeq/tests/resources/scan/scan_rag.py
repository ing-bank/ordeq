from pprint import pprint

import example_rag_pipeline
from ordeq._scan import scan

nodes, ios = scan(example_rag_pipeline)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))
