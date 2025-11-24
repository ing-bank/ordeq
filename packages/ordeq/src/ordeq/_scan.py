from collections import defaultdict
from collections.abc import Callable
from types import ModuleType

from ordeq._fqn import FQ, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import Node, _is_node


def scan(*modules: ModuleType) -> tuple[list[FQ[Node]], list[FQ[AnyIO]]]:
    nodes: dict[Callable, list[FQ[Node]]] = defaultdict(list)
    ios: dict[IOIdentity, list[FQ[AnyIO]]] = defaultdict(list)
    for module in modules:
        for name, obj in vars(module).items():
            if _is_io(obj):
                io_id = id(obj)
                if io_id in ios:
                    fqn, _ = ios[io_id][0]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases IO "
                            f"'{existing_ref}' to '{name}'. "
                            f"IOs cannot be aliased."
                        )
                ios[io_id].append(((module.__name__, name), obj))
            elif _is_node(obj):
                if obj in nodes:
                    fqn, _ = nodes[obj][0]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        raise ValueError(
                            f"Module '{module.__name__}' aliases node "
                            f"'{existing_ref}' to '{name}'. "
                            f"Nodes cannot be aliased."
                        )
                nodes[obj].append(((module.__name__, name), obj))
    return (
        [fq_node for node_list in nodes.values() for fq_node in node_list],
        [fq_io for io_list in ios.values() for fq_io in io_list],
    )
