# Captures the behaviour when resolving a module containing the same names
# for the same node.

from example_duplicates import duplicate_node_names
from ordeq._resolve import _resolve_module_to_nodes

_ = _resolve_module_to_nodes(duplicate_node_names)
