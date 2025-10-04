from collections.abc import Callable, Hashable
from types import ModuleType

from ordeq.framework._registry import NODE_REGISTRY
from ordeq.framework.nodes import Node, get_node


def _gather_nodes_from_module(module: ModuleType) -> list[Node]:
    """Gathers all nodes defined in a module.

    Args:
        module: the module to gather nodes from

    Returns:
        a list of nodes defined in the module

    """

    nodes = []
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, Hashable) and obj in NODE_REGISTRY:
            nodes.append(NODE_REGISTRY.get(obj))
    return nodes


def _collect_nodes(*runnables: ModuleType | Callable) -> list[Node]:
    """Collects nodes from the provided runnables.

    Args:
        runnables: modules or callables to gather nodes from

    Returns:
        a list of nodes collected from the runnables

    Raises:
        TypeError: if runnables are not all modules or all callables
    """
    if all(isinstance(r, ModuleType) for r in runnables):
        modules: tuple[ModuleType, ...] = runnables  # type: ignore[assignment]
        nodes = []
        for module in modules:
            nodes.extend(_gather_nodes_from_module(module))
        return nodes

    if all(callable(r) for r in runnables):
        funcs: tuple[Callable, ...] = runnables  # type: ignore[assignment]
        return [get_node(func) for func in funcs]

    raise TypeError("All runnables must be either modules or nodes.")
