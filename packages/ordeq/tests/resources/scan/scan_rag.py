from pprint import pprint

import example_rag_pipeline
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(example_rag_pipeline)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)
