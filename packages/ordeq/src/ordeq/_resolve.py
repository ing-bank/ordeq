"""Resolve packages and modules to nodes and IOs."""

from __future__ import annotations

import importlib
import pkgutil
import warnings
from collections.abc import Generator
from types import ModuleType
from typing import TypeAlias, TypeGuard

from ordeq._fqn import FQN, ModuleName, ObjectRef, is_object_ref
from ordeq._hook import NodeHook, RunHook, RunnerHook
from ordeq._io import AnyIO, _is_io, _is_io_sequence
from ordeq._nodes import Node, _is_node

RunnableRef: TypeAlias = ObjectRef | ModuleName
Runnable: TypeAlias = ModuleType | Node
Catalog: TypeAlias = dict[str, dict[str, AnyIO]]


def _is_module(obj: object) -> TypeGuard[ModuleType]:
    return isinstance(obj, ModuleType)


def _validate_runnables(*runnables: Runnable | RunnableRef) -> None:
    for runnable in runnables:
        if not (
            _is_module(runnable)
            or _is_node(runnable)
            or isinstance(runnable, str)
        ):
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a node, got "
                f"{type(runnable).__name__}"
            )


def _deduplicate_modules(*modules: ModuleType) -> Generator[ModuleType]:
    visited = set()
    for module in modules:
        if module.__name__ in visited:
            warnings.warn(
                f"Module '{module.__name__}' was provided more than once. "
                f"Duplicates will be ignored.",
                stacklevel=2,
            )
        visited.add(module.__name__)
        yield module


def _is_package(module: ModuleType) -> TypeGuard[ModuleType]:
    return hasattr(module, "__path__")


def _resolve_module_ref_to_module(module_ref: ModuleName) -> ModuleType:
    return importlib.import_module(module_ref)


def _resolve_fqn_to_node(fqn: FQN) -> Node:
    module_ref, node_name = fqn
    module = _resolve_module_ref_to_module(module_ref)
    node_obj = getattr(module, node_name, None)
    if node_obj is None or not _is_node(node_obj):
        raise ValueError(
            f"Node '{node_name}' not found in module '{module_ref}'"
        )
    return node_obj


def _resolve_fqn_to_hook(fqn: FQN) -> RunnerHook:
    module_ref, hook_name = fqn
    module = _resolve_module_ref_to_module(module_ref)
    hook_obj = getattr(module, hook_name, None)
    if hook_obj is None or not isinstance(hook_obj, (NodeHook, RunHook)):
        raise ValueError(
            f"Hook '{hook_name}' not found in module '{module_ref}'"
        )
    return hook_obj


def _resolve_fqn_to_io(fqn: FQN) -> AnyIO:
    module_ref, io_name = fqn
    module = _resolve_module_ref_to_module(module_ref)
    io_obj = getattr(module, io_name, None)
    if io_obj is None or not _is_io(io_obj):
        raise ValueError(f"IO '{io_name}' not found in module '{module_ref}'")
    return io_obj


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
    def _walk(module: ModuleType):
        yield module
        if _is_package(module):
            for subname in _resolve_package_to_module_names(module):
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
                f"Expected a module or a string, got "
                f"{type(runnable).__name__}"
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


def _resolve_hook_refs(*hooks: str | RunnerHook) -> list[RunnerHook]:
    resolved_hooks = []
    for hook in hooks:
        if isinstance(hook, (NodeHook, RunHook)):
            resolved_hooks.append(hook)
        elif isinstance(hook, str):
            fqn = FQN.from_ref(hook)
            resolved_hook = _resolve_fqn_to_hook(fqn)
            resolved_hooks.append(resolved_hook)
        else:
            raise TypeError(
                f"{hook} is not a valid hook reference. "
                f"Expected a RunnerHook or a string, got "
                f"{type(hook).__name__}"
            )
    return resolved_hooks


def _split_runner_hooks(
    *hooks: RunnerHook,
) -> tuple[list[RunHook], list[NodeHook]]:
    run_hooks = []
    node_hooks = []
    for hook in hooks:
        if isinstance(hook, NodeHook):
            node_hooks.append(hook)
        elif isinstance(hook, RunHook):
            run_hooks.append(hook)
    return run_hooks, node_hooks


def _resolve_refs_to_hooks(
    *hooks: str | RunnerHook,
) -> tuple[list[RunHook], list[NodeHook]]:
    resolved_hooks = _resolve_hook_refs(*hooks)
    return _split_runner_hooks(*resolved_hooks)


def _resolve_runnables_to_nodes_and_modules(
    *runnables: Runnable | RunnableRef,
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
        elif _is_node(runnable):
            if runnable not in nodes:
                nodes.append(runnable)
            else:
                warnings.warn(
                    f"Node '{runnable.ref}' already provided in another "
                    f"runnable",
                    stacklevel=2,
                )
        elif isinstance(runnable, str):
            fqn = FQN.from_ref(runnable)
            node = _resolve_fqn_to_node(fqn)
            if node not in nodes:
                nodes.append(node)
            else:
                warnings.warn(
                    f"Node '{node.ref}' already provided in another runnable",
                    stacklevel=2,
                )
        else:
            raise TypeError(
                f"{runnable} is not something we can run. "
                f"Expected a module or a node, got "
                f"{type(runnable).__name__}"
            )

    modules = list(_resolve_refs_to_modules(*modules_and_strs))
    return nodes, modules


def _resolve_module_to_nodes(module: ModuleType) -> dict[str, Node]:
    nodes: dict[Node, str] = {}
    for name, obj in vars(module).items():
        if _is_node(obj):
            if obj in nodes:
                raise ValueError(
                    f"Module '{module.__name__}' contains duplicate keys "
                    f"for the same node ('{name}' and '{nodes[obj]}')"
                )
            nodes[obj] = name
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


def _resolve_runnables_to_nodes_and_ios(
    *runnables: Runnable | RunnableRef,
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
        if node.module:
            module = _resolve_module_ref_to_module(node.module)
            ios.update({node.module: _resolve_module_to_ios(module)})

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


def _resolve_modules_to_nodes(*modules: ModuleType) -> list[Node]:
    nodes: list[Node] = []
    for module in _resolve_packages_to_modules(*modules):
        nodes.extend(_resolve_module_to_nodes(module).values())
    return nodes


def _resolve_runnable_refs_to_nodes(
    *runnables: RunnableRef | Runnable,
) -> list[Node]:
    nodes: list[Node] = []
    for runnable in runnables:
        if _is_node(runnable):
            nodes.append(runnable)
        elif isinstance(runnable, str) and is_object_ref(runnable):
            fqn = FQN.from_ref(runnable)
            nodes.append(_resolve_fqn_to_node(fqn))
    return nodes


def _resolve_runnable_refs_to_modules(
    *runnables: RunnableRef | Runnable,
) -> list[ModuleType]:
    modules: list[ModuleType] = []
    for runnable in runnables:
        if _is_module(runnable):
            modules.append(runnable)
        elif isinstance(runnable, str) and not is_object_ref(runnable):
            modules.append(_resolve_module_ref_to_module(runnable))
    return modules


def _resolve_module_name_to_module(
    module: ModuleType | ModuleName,
) -> ModuleType:
    if _is_module(module):
        # (ty false positive)
        return module  # type: ignore[invalid-return-type]
    if isinstance(module, str):
        return _resolve_module_ref_to_module(module)
    raise TypeError(
        f"'{module}' is not a valid module. "
        f"Expected a ModuleType or a string, got "
        f"{type(module).__name__}"
    )
