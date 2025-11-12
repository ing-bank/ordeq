# Captures the behaviour when resolving a module containing the same object
from example_duplicates import duplicate_node_objects
from ordeq._resolve import _resolve_module_to_nodes

_ = _resolve_module_to_nodes(duplicate_node_objects)
