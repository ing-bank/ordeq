import importlib
import pkgutil
from collections.abc import Callable, Hashable
from types import ModuleType

from ordeq.framework._registry import NODE_REGISTRY
from ordeq.framework.io import IO, Input, Output
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


def _collect_nodes(*runnables: ModuleType | Callable | str) -> list[Node]:
    """Collects nodes from the provided runnables.

    Args:
        runnables: modules or callables to gather nodes from

    Returns:
        a list of nodes collected from the runnables

    Raises:
        TypeError: if a runnable is not a module and not a node
    """

    nodes = []
    for runnable in runnables:
        if isinstance(runnable, ModuleType):
            nodes.extend(_gather_nodes_from_module(runnable))
        elif callable(runnable):
            nodes.append(get_node(runnable))
        else:
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a node, got {type(runnable)}"
            )
    return nodes


def _gather_ios_from_module(
    module: ModuleType,
) -> dict[str, IO | Input | Output]:
    """Find all `IO` objects defined in the provided module

    Args:
        module: the Python module object

    Returns:
        a dict of `IO` objects with their variable name as key
    """
    return {
        k: v
        for k, v in vars(module).items()
        if isinstance(v, (IO, Input, Output))
    }


def _gather_nodes_from_registry() -> set[Node]:
    """Find all `Node` objects defined in the provided module

    Returns:
        a set of `Node` objects
    """
    return set(NODE_REGISTRY._data.values())  # noqa: SLF001


def _gather_nodes_and_ios_from_package(
    package: ModuleType,
) -> tuple[set[Node], dict[str, IO | Input | Output]]:
    """Gather all nodes and IOs from the provided package.

    Args:
        package: the Python package object

    Returns:
        a tuple of a set of `Node` objects and a dict of `IO` objects
    """
    module_names = [
        name for _, name, _ in pkgutil.iter_modules(package.__path__)
    ]
    modules = [
        importlib.import_module(f".{name}", package=package.__name__)
        for name in module_names
    ]
    ios = {}
    for m in modules:
        ios.update(_gather_ios_from_module(m))

    # Gather nodes from the registry
    nodes = _gather_nodes_from_registry()
    return nodes, ios


def _collect_nodes_and_ios(
    *runnables: str | ModuleType | Callable,
) -> tuple[set[Node], dict[str, IO | Input | Output]]:
    """Collects nodes and IOs from the provided runnables.

    Args:
        runnables: package names, modules, or callables to gather nodes and IOs
            from

    Returns:
        a tuple of nodes and IOs collected from the runnables

    Raises:
        TypeError: if runnables are not all modules, all package names,
            or all nodes
    """
    if all(isinstance(r, ModuleType) for r in runnables):
        module_types: tuple[ModuleType, ...] = runnables  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for module in module_types:
            nodes.update(_gather_nodes_from_module(module))
            ios.update(_gather_ios_from_module(module))

        return nodes, ios
    if all(isinstance(r, str) for r in runnables):
        package_names: tuple[str, ...] = runnables  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for package in package_names:
            package_mod = importlib.import_module(package)
            nodes.update(_gather_nodes_from_module(package_mod))
            package_nodes, package_ios = _gather_nodes_and_ios_from_package(
                package_mod
            )
            nodes.update(package_nodes)
            ios.update(package_ios)

        return nodes, ios

    if all(callable(r) for r in runnables):
        callables: tuple[Callable, ...] = runnables  # type: ignore[assignment]
        nodes = {get_node(func) for func in callables}
        ios = {}
        for node in nodes:
            mod = importlib.import_module(node.func.__module__)
            ios.update(_gather_ios_from_module(mod))

        return nodes, ios

    raise TypeError(
        "All objects provided must be either modules, package names, or nodes."
    )
