"""Resolve packages and modules to nodes and IOs."""

from __future__ import annotations

import importlib
import pkgutil
import warnings
from collections.abc import Generator, Sequence
from types import ModuleType
from typing import TYPE_CHECKING, Any, TypeAlias, TypeGuard

from ordeq._fqn import (
    FQNamed,
    ModuleRef,
    ObjectRef,
    fqn_to_object_ref,
    is_object_ref,
    object_ref_to_fqn,
)
from ordeq._hook import NodeHook, RunHook, RunnerHook
from ordeq._io import IO, AnyIO, Input, Output
from ordeq._nodes import Node, View, get_node

if TYPE_CHECKING:
    from ordeq._runner import Runnable

Catalog: TypeAlias = dict[str, dict[str, AnyIO]]


def _is_module(obj: object) -> TypeGuard[ModuleType]:
    return isinstance(obj, ModuleType)


def _is_package(module: ModuleType) -> TypeGuard[ModuleType]:
    return hasattr(module, "__path__")


def _is_io(obj: object) -> TypeGuard[AnyIO]:
    return isinstance(obj, (IO, Input, Output))


def _resolve_module_ref_to_module(module_ref: ModuleRef) -> ModuleType:
    return importlib.import_module(module_ref)


def _is_node(obj: object) -> bool:
    return (
        callable(obj)
        and hasattr(obj, "__ordeq_node__")
        and isinstance(obj.__ordeq_node__, Node)
    )


def _resolve_object_ref_to_node(ref: ObjectRef) -> FQNamed[Node]:
    module_ref, node_name = object_ref_to_fqn(ref)
    module = _resolve_module_ref_to_module(module_ref)
    node_obj = getattr(module, node_name, None)
    if node_obj is None or not _is_node(node_obj):
        raise ValueError(
            f"Node '{node_name}' not found in module '{module_ref}'"
        )
    return module_ref, node_name, get_node(node_obj)


def _resolve_object_ref_to_hook(ref: ObjectRef) -> FQNamed[RunnerHook]:
    module_ref, hook_name = object_ref_to_fqn(ref)
    module = _resolve_module_ref_to_module(module_ref)
    hook_obj = getattr(module, hook_name, None)
    if hook_obj is None or not isinstance(hook_obj, (NodeHook, RunHook)):
        raise ValueError(
            f"Hook '{hook_name}' not found in module '{module_ref}'"
        )
    return module_ref, hook_name, hook_obj


def _resolve_object_ref_to_io(ref: ObjectRef) -> FQNamed[AnyIO]:
    module_ref, io_name = object_ref_to_fqn(ref)
    module = _resolve_module_ref_to_module(module_ref)
    io_obj = getattr(module, io_name, None)
    if io_obj is None or not _is_io(io_obj):
        raise ValueError(f"IO '{io_name}' not found in module '{module_ref}'")
    return module_ref, io_name, io_obj


def _resolve_sequence_to_ios(value: Any) -> list[AnyIO]:
    if _is_io(value):
        return [value]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [io for v in value for io in _resolve_sequence_to_ios(v)]
    if isinstance(value, dict):
        return [
            io for v in value.values() for io in _resolve_sequence_to_ios(v)
        ]
    return []


def _is_io_sequence(value: Any) -> bool:
    return bool(_resolve_sequence_to_ios(value))


def _resolve_package_to_module_names(package: ModuleType) -> Generator[str]:
    yield from (
        f"{package.__name__}.{name}"
        for _, name, _ in pkgutil.iter_modules(package.__path__)
    )


def _resolve_module_globals(
    module: ModuleType,
) -> dict[str, AnyIO | Node | list[AnyIO]]:
    """Gathers all IOs and nodes defined in a module.

    Args:
        module: the module to gather IOs and nodes from

    Returns:
        a dict of all IOs and nodes defined in the module
    """
    return {
        name: obj
        for name, obj in vars(module).items()
        if _is_io(obj) or _is_node(obj) or _is_io_sequence(obj)
    }


def _resolve_packages_to_modules(
    *modules: ModuleType,
) -> Generator[ModuleType, None, None]:
    visited = set()

    def _walk(module: ModuleType):
        if module.__name__ in visited:
            warnings.warn(
                f"Module '{module.__name__}' already provided as runnable",
                stacklevel=2,
            )
            return
        visited.add(module.__name__)
        yield module
        if _is_package(module):
            for subname in _resolve_package_to_module_names(module):
                if subname in visited:
                    warnings.warn(
                        f"Module '{subname}' already provided as runnable",
                        stacklevel=2,
                    )
                    continue
                submodule = _resolve_module_ref_to_module(subname)
                yield from _walk(submodule)

    for module in modules:
        yield from _walk(module)


def _resolve_refs_to_modules(
    *runnables: str | ModuleType,
) -> Generator[ModuleType]:
    modules: list[ModuleType] = []
    for runnable in runnables:
        if _is_module(runnable):
            if runnable not in modules:
                modules.append(runnable)
            else:
                warnings.warn(
                    f"Module '{runnable.__name__}' already provided as "
                    f"runnable",
                    stacklevel=2,
                )
        elif isinstance(runnable, str):
            mod = _resolve_module_ref_to_module(runnable)
            if mod not in modules:
                modules.append(mod)
            else:
                warnings.warn(
                    f"Module '{runnable}' already provided as runnable",
                    stacklevel=2,
                )
        else:
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a string, got {type(runnable)}"
            )

    # Then, for each module or package, if it's a package, resolve to all its
    # submodules recursively
    return _resolve_packages_to_modules(*modules)


def _resolve_module_to_ios(module: ModuleType) -> dict[str, AnyIO]:
    ios: dict[AnyIO, str] = {}
    for name, obj in vars(module).items():
        if _is_io(obj):
            # TODO: Should also resolve to IO sequence
            if obj in ios:
                raise ValueError(
                    f"Module '{module.__name__}' contains duplicate keys "
                    f"for the same IO ('{name}' and '{ios[obj]}')"
                )
            ios[obj] = name
    return {name: io for io, name in ios.items()}


def _resolve_package_to_ios(package: ModuleType) -> Catalog:
    """Finds all `IO` objects defined in the provided module or package.

    Args:
        package: the module or package

    Returns:
        a dict of `IO` objects with their fully-qualified name as key
    """
    modules = _resolve_packages_to_modules(package)
    catalog = {}
    for module in modules:
        catalog.update({module.__name__: _resolve_module_to_ios(module)})
    return {module_name: ios for module_name, ios in catalog.items() if ios}


def _resolve_refs_to_hooks(
    *hooks: str | RunnerHook,
) -> tuple[list[RunHook], list[NodeHook]]:
    run_hooks = []
    node_hooks = []
    for hook in hooks:
        if isinstance(hook, NodeHook):
            node_hooks.append(hook)
        elif isinstance(hook, RunHook):
            run_hooks.append(hook)
        elif isinstance(hook, str):
            _, _, resolved_hook = _resolve_object_ref_to_hook(hook)
            if isinstance(resolved_hook, NodeHook):
                node_hooks.append(resolved_hook)
            elif isinstance(resolved_hook, RunHook):
                run_hooks.append(resolved_hook)
    return run_hooks, node_hooks


def _resolve_runnables_to_nodes_and_modules(
    *runnables: Runnable,
) -> tuple[list[Node], list[ModuleType]]:
    """Collects nodes and modules from the provided runnables.

    Args:
        runnables: modules, packages, node references or callables to gather
            nodes from

    Returns:
        the nodes and modules collected from the runnables

    Raises:
        TypeError: if a runnable is not a module and not a node
    """
    modules_and_strs: list[ModuleType | str] = []
    nodes: list[Node] = []
    for runnable in runnables:
        if _is_module(runnable) or (
            isinstance(runnable, str) and not is_object_ref(runnable)
        ):
            # mypy false positive
            modules_and_strs.append(runnable)  # type: ignore[arg-type]
        elif callable(runnable):
            node = get_node(runnable)
            if node not in nodes:
                nodes.append(node)
            else:
                warnings.warn(
                    f"Node '{node.name}' already provided in another runnable",
                    stacklevel=2,
                )
        elif isinstance(runnable, str):
            module_ref, node_name, node = _resolve_object_ref_to_node(runnable)
            if node not in nodes:
                nodes.append(node)
            else:
                warnings.warn(
                    f"Node '{fqn_to_object_ref((module_ref, node_name))}' "
                    f"already provided in another runnable",
                    stacklevel=2,
                )
        else:
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a node, got {type(runnable)}"
            )

    modules = list(_resolve_refs_to_modules(*modules_and_strs))
    return nodes, modules


def _resolve_module_to_nodes(module: ModuleType) -> dict[str, Node]:
    nodes: dict[Node, str] = {}
    for name, obj in vars(module).items():
        if _is_node(obj):
            node = get_node(obj)
            if node in nodes:
                raise ValueError(
                    f"Module '{module.__name__}' contains duplicate keys "
                    f"for the same node ('{name}' and '{nodes[node]}')"
                )
            nodes[node] = name
    return {name: node for node, name in nodes.items()}


def _resolve_runnables_to_nodes(*runnables: Runnable) -> list[Node]:
    """Collects nodes from the provided runnables.

    Args:
        runnables: modules, packages, node references or callables to gather
            nodes from

    Returns:
        the nodes collected from the runnables

    """
    nodes, modules = _resolve_runnables_to_nodes_and_modules(*runnables)
    for module in modules:
        nodes.extend(_resolve_module_to_nodes(module).values())
    return nodes


def _check_missing_ios(nodes: set[Node], ios: Catalog) -> None:
    missing_ios: set[AnyIO | View] = set()
    for node in nodes:
        for inp in node.inputs:
            if inp not in ios.values():
                missing_ios.add(inp)
        for out in node.outputs:
            if out not in ios.values():
                missing_ios.add(out)

    if missing_ios:
        raise ValueError(
            f"The following IOs are used by nodes but not defined: "
            f"{missing_ios}. Please include the module defining them in "
            f"the runnables."
        )


def _resolve_runnables_to_nodes_and_ios(
    *runnables: Runnable,
) -> tuple[list[Node], Catalog]:
    """Collects nodes and IOs from the provided runnables.

    Args:
        runnables: modules, packages, node references or callables to gather
            nodes and IOs from

    Returns:
        a tuple of nodes and IOs collected from the runnables
    """

    ios = {}
    nodes, modules = _resolve_runnables_to_nodes_and_modules(*runnables)

    for node in nodes:
        mod = _resolve_module_ref_to_module(node.func.__module__)
        ios.update({mod.__name__: _resolve_module_to_ios(mod)})

    for module in modules:
        nodes.extend(_resolve_module_to_nodes(module).values())
        ios.update({module.__name__: _resolve_module_to_ios(module)})

    # Filter empty IO modules
    ios = {
        module_name: ios_dict
        for module_name, ios_dict in ios.items()
        if ios_dict
    }
    return nodes, ios
