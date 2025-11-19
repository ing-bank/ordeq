from mypy.moduleinspect import ModuleType

from ordeq._fqn import FQ, ModuleRef, fqn_to_object_ref
from ordeq._io import AnyIO, IOIdentity, _is_io
from ordeq._nodes import Node, _is_node, get_node
from ordeq._resolve import _resolve_packages_to_modules

RootType = ModuleRef | ModuleType


def scan(root: ModuleType) -> tuple[list[FQ[Node]], list[FQ[AnyIO]]]:
    modules = _resolve_packages_to_modules(root)
    nodes: list[FQ[Node]] = []
    ios: dict[IOIdentity, FQ[AnyIO]] = {}
    for module in modules:
        for name, obj in vars(module).items():
            if _is_io(obj):
                io_id = id(obj)
                io_ref = fqn_to_object_ref((module.__name__, name))
                if io_id in ios:
                    fqn, _ = ios[io_id]
                    existing_ref = fqn_to_object_ref(fqn)
                    if name != fqn[1]:
                        raise ValueError(
                            f"'{root.__name__}' contains duplicate keys "
                            f"for the same IO ('{io_ref}' and "
                            f"'{existing_ref}')"
                        )
                ios[io_id] = ((module.__name__, name), obj)
            elif _is_node(obj):
                nodes.append(((module.__name__, name), get_node(obj)))
    return nodes, list(ios.values())
