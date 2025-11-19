from collections import defaultdict
from types import ModuleType

from ordeq._fqn import FQ, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import Node, _is_node, get_node
from ordeq._resolve import _resolve_packages_to_modules


def scan(root: ModuleType) -> tuple[list[FQ[Node]], list[FQ[AnyIO]]]:
    modules = _resolve_packages_to_modules(root)
    nodes: list[FQ[Node]] = []
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
                nodes.append(((module.__name__, name), get_node(obj)))
    return nodes, [fqn_io for io_list in ios.values() for fqn_io in io_list]
