import ast
import importlib
import pathlib
import pkgutil
from collections.abc import Generator, Hashable
from types import ModuleType

from ordeq import IO, Input, Output
from ordeq.framework._registry import (
    NODE_REGISTRY,  # noqa: PLC2701 (private-member-access)
)
from ordeq.framework.nodes import get_node

from ordeq_manifest.models import IOModel, NodeModel


def gather_modules(module: ModuleType) -> Generator[ModuleType, None, None]:
    """Gathers all modules from a given module or package (recursively).

    Args:
        module: The module or package.

    Yields:
        All modules in the module/package.
    """

    yield module
    if hasattr(module, "__path__"):  # It's a package
        package = module
        for _, name, _ in pkgutil.iter_modules(package.__path__):
            submodule = importlib.import_module(f"{package.__name__}.{name}")
            yield from gather_modules(submodule)


def gather_objects(
    module: ModuleType,
) -> Generator[tuple[ModuleType, str, object], None, None]:
    """Gathers all objects from a given module ir package (recursively).

    Args:
        module: The module to gather objects from.

    Yields:
        All objects in the module/package.
    """

    for m in gather_modules(module):
        for name, value in vars(m).items():
            yield m, name, value


def load_ast(module: ModuleType) -> ast.Module:
    with pathlib.Path(module.__file__).open("r", encoding="utf-8") as f:
        return ast.parse(f.read(), filename=__file__)


def compute_symbol_table(package: ModuleType) -> dict[str, str]:
    symbol_table: dict[str, str] = {}
    for module in gather_modules(package):
        if module.__file__ and module.__file__.endswith(".py"):
            tree = load_ast(module)
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    mod = node.module
                    for alias in node.names:
                        local_name = alias.asname or alias.name
                        symbol_table[f"{module.__name__}.{local_name}"] = (
                            f"{mod}.{alias.name}"
                        )
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        local_name = alias.asname or alias.name
                        symbol_table[f"{module.__name__}.{local_name}"] = (
                            alias.name
                        )
    return symbol_table


def gather(
    module_or_package: ModuleType,
) -> tuple[dict[str, NodeModel], dict[str, IOModel]]:
    """Gathers all nodes and IOs from a given module or package (recursively).

    Args:
        module_or_package: The module or package to search.

    Returns:
        Tuple of dict from ID to NodeModel, and dict from ID to IOModel.
    """

    io_models_by_id: dict[str, IOModel] = {}
    ios_to_id: dict[IO | Input | Output, str] = {}
    node_models_by_id: dict[str, NodeModel] = {}

    symbol_table = compute_symbol_table(module_or_package)

    for module, name, value in gather_objects(module_or_package):
        if isinstance(value, (IO, Input, Output)):
            fqn = f"{module.__name__}.{name}"
            idx = symbol_table.get(fqn, fqn)
            t = type(value)
            io_model = IOModel(
                id=idx, name=name, type=f"{t.__module__}.{t.__name__}"
            )
            if idx not in io_models_by_id:
                io_models_by_id[idx] = io_model
            ios_to_id[value] = idx
        elif isinstance(value, Hashable) and value in NODE_REGISTRY:
            fqn = f"{module.__name__}.{name}"
            idx = symbol_table.get(fqn, fqn)
            node = get_node(value)
            node_models_by_id[idx] = NodeModel(
                id=idx,
                name=name,
                inputs=[ios_to_id[i] for i in node.inputs],
                outputs=[ios_to_id[o] for o in node.outputs],
                tags=node.tags,
            )
    return node_models_by_id, io_models_by_id
