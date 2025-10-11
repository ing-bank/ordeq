import importlib
import pkgutil
from types import ModuleType

from ordeq import IO, Input, Node, Output
from ordeq._nodes import get_node  # noqa: PLC2701 (private-member-access)
from ordeq._resolve import (
    _is_node_proxy,  # noqa: PLC2701 (private-member-access)
)


def _gather_modules(module: ModuleType):
    modules = [module]
    if hasattr(module, "__path__"):  # It's a package
        package = module
        for _, name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{package.__name__}.{name}")
            modules.extend(_gather_modules(module))
    return modules


def gather_nodes(module_or_package: ModuleType) -> dict[str, Node]:
    """Gathers all nodes from a given module or package (recursively).

    Args:
        module_or_package: The module or package to search.

    Returns:
        Dictionary of node names to instances for the given module/package.
    """

    modules = _gather_modules(module_or_package)
    nodes: dict[str, Node] = {}
    for module in modules:
        for k, v in vars(module).items():
            if _is_node_proxy(v):
                node = get_node(v)
                nodes[f"{module.__name__}.{k}"] = node
    return nodes


def gather_ios(
    module_or_package: ModuleType,
) -> dict[str, IO | Input | Output]:
    """Gathers all Input, Output and IO instances from a given module or
    package (recursively).

    Args:
        module_or_package: The module or package to search.

    Returns:
        Dictionary of IO names to instances for the given module/package.
    """

    ios: dict[str, IO | Input | Output] = {}

    for module in _gather_modules(module_or_package):
        for k, v in vars(module).items():
            if isinstance(v, (Input, Output, IO)):
                ios[f"{module.__name__}.{k}"] = v
    return ios
