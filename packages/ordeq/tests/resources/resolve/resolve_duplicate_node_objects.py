# Captures the behaviour when resolving a module containing the same object
from pprint import pprint

from example_duplicates import duplicate_node_objects
from ordeq._resolve import _resolve_module_to_nodes

nodes = _resolve_module_to_nodes(duplicate_node_objects)
pprint(nodes)
