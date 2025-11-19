from mypy.moduleinspect import ModuleType

from ordeq._fqn import FQ, ModuleRef
from ordeq._io import AnyIO
from ordeq._nodes import Node
from ordeq._resolve import (
    _resolve_module_to_ios,
    _resolve_module_to_nodes,
    _resolve_packages_to_modules,
)

RootType = ModuleRef | ModuleType


def scan(root: ModuleType) -> tuple[list[FQ[Node]], list[FQ[AnyIO]]]:
    modules = _resolve_packages_to_modules(root)
    nodes: list[FQ[Node]] = []
    ios: list[FQ[AnyIO]] = []
    for module in modules:
        ios.extend(
            ((module.__name__, io_name), io)
            for io_name, io in _resolve_module_to_ios(module).items()
        )
        nodes.extend(
            ((module.__name__, node_name), node)
            for node_name, node in _resolve_module_to_nodes(module).items()
        )
    return nodes, ios
