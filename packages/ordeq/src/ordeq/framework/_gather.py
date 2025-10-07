import importlib
import pkgutil
from collections.abc import Callable, Generator, Hashable, Iterable
from types import ModuleType

from ordeq.framework._registry import NODE_REGISTRY
from ordeq.framework.io import IO, Input, Output
from ordeq.framework.nodes import Node, get_node


def _is_module(obj: object) -> bool:
    return isinstance(obj, ModuleType)


def _is_package(module: ModuleType) -> bool:
    return hasattr(module, "__path__")


def _is_io(obj: object) -> bool:
    return isinstance(obj, (IO, Input, Output))


def _is_node(obj: object) -> bool:
    return isinstance(obj, Hashable) and obj in NODE_REGISTRY


def _resolve_string_to_module(name: str) -> ModuleType:
    return importlib.import_module(name)


def _resolve_packages_to_modules(
    modules: Iterable[ModuleType],
) -> Generator[ModuleType, None, None]:
    for module in modules:
        yield module
        if _is_package(module):
            submodules = (
                importlib.import_module(f".{name}", package=module.__name__)
                for _, name, _ in pkgutil.iter_modules(module.__path__)
            )
            yield from _resolve_packages_to_modules(submodules)


def _resolve_runnables_to_modules(
    *runnables: str | ModuleType,
) -> Generator[ModuleType, None, None]:
    # First, resolve all strings to modules or packages
    packaged_and_modules = (
        _resolve_string_to_module(r) if isinstance(r, str) else r
        for r in runnables
    )

    # Then, for each module or package, if it's a package, resolve to all its
    # submodules recursively
    return _resolve_packages_to_modules(packaged_and_modules)


def _resolve_module_to_nodes(module: ModuleType) -> set[Node]:
    """Gathers all nodes defined in a module.

    Args:
        module: the module to gather nodes from

    Returns:
        the nodes defined in the module

    """

    return {get_node(obj) for obj in vars(module).values() if _is_node(obj)}


def _resolve_module_to_ios(
    module: ModuleType,
) -> dict[str, IO | Input | Output]:
    """Find all `IO` objects defined in the provided module

    Args:
        module: the Python module object

    Returns:
        a dict of `IO` objects with their variable name as key
    """
    return {name: obj for name, obj in vars(module).items() if _is_io(obj)}


def _resolve_runnables_to_nodes(
    *runnables: ModuleType | Callable | str,
) -> set[Node]:
    """Collects nodes from the provided runnables.

    Args:
        runnables: modules, packages or callables to gather nodes from

    Returns:
        the nodes collected from the runnables

    Raises:
        TypeError: if a runnable is not a module and not a node
    """

    # Split runnables into modules/strings and callables
    modules_and_strs = []
    nodes = set()
    for runnable in runnables:
        if isinstance(runnable, (ModuleType, str)):
            modules_and_strs.append(runnable)
        elif callable(runnable):
            nodes.add(get_node(runnable))
        else:
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a node, got {type(runnable)}"
            )

    modules = _resolve_runnables_to_modules(*modules_and_strs)
    for module in modules:
        nodes.update(_resolve_module_to_nodes(module))

    return nodes


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
        ios.update(_resolve_module_to_ios(m))

    # Gather nodes from the registry
    nodes = _gather_nodes_from_registry()
    return nodes, ios


def _resolve_runnables_to_nodes_and_ios(
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
            nodes.update(_resolve_module_to_nodes(module))
            ios.update(_resolve_module_to_ios(module))

        return nodes, ios
    if all(isinstance(r, str) for r in runnables):
        package_names: tuple[str, ...] = runnables  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for package in package_names:
            package_mod = importlib.import_module(package)
            nodes.update(_resolve_module_to_nodes(package_mod))
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
            ios.update(_resolve_module_to_ios(mod))

        return nodes, ios

    raise TypeError(
        "All objects provided must be either modules, package names, or nodes."
    )
