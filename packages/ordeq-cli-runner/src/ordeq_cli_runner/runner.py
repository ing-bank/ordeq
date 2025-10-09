import importlib
from collections.abc import Callable
from types import ModuleType

from ordeq import NodeHook, run
from ordeq._runner import DataStoreType, SaveMode


def get_module(module_ref: str) -> ModuleType:
    """Function that loads a module based on a reference string

    Args:
        module_ref: reference to the module, e.g. "my.module"

    Returns:
        the module object

    Raises:
        ModuleNotFoundError: if the module is not found
    """

    try:
        return importlib.import_module(module_ref)
    except ModuleNotFoundError:
        raise


def get_obj(
    ref: str, _get_module: Callable[[str], ModuleType] = get_module
) -> object:
    """Gets an object based on its reference. The reference should be
    formatted ``{package}.{subpackage}.{...}:{name}``. Used to retrieve
    nodes and pipelines based on references provided to the CLI.

    Examples:

    ```python
    >>> from ordeq import Node
    >>> node = get_obj("path.to.module:export_to_mssql")  # doctest: +SKIP
    >>> isinstance(node, Node)  # doctest: +SKIP
    True

    >>> pipeline = get_obj("path.to.module:everything")  # doctest: +SKIP
    >>> isinstance(pipeline, set) # doctest: +SKIP
    True
    >>> all(callable(o) for o in pipeline) # doctest: +SKIP
    True

    >>> from ordeq._hook import Hook
    >>> log_hook = get_obj("path.to.module:LogHook")  # doctest: +SKIP
    >>> isinstance(log_hook, Hook)  # doctest: +SKIP
    True
    ```

    Args:
        ref: reference to the object
        _get_module: method to retrieve the module of the object

    Returns:
        the object

    Raises:
        ModuleNotFoundError: if the module cannot be found
        AttributeError: if the object is not found in the module.
    """

    module_ref, _, node_name = ref.partition(":")
    try:
        module = _get_module(module_ref)
    except ModuleNotFoundError:
        raise
    try:
        return getattr(module, node_name)
    except AttributeError:
        raise


def get_node(
    ref: str, _get_obj: Callable[[str], object] = get_obj
) -> Callable:
    """Gets a node based on its reference. The reference should be
    formatted ``{package}.{subpackage}.{...}:{name}``. Used to retrieve a
    node based on a reference provided to the CLI.

    Args:
        ref: the node reference
        _get_obj: callable to get an object based on its reference

    Returns:
         the node

     Raises:
         TypeError: if the retrieved object is not a node.
    """

    obj = _get_obj(ref)
    if not callable(obj):
        msg = f"'{ref}' is not a node"
        raise TypeError(msg)
    return obj


def get_pipeline(
    ref: str, _get_obj: Callable[[str], object] = get_obj
) -> set[Callable]:
    """Gets a pipeline based on its reference. The reference should be
    formatted ``{package}.{subpackage}.{...}:{name}``. Used to retrieve a
    pipeline based on a reference provided to the CLI.

    Args:
        ref: the pipeline reference
        _get_obj: callable to get an object based on its reference

    Returns:
        the pipeline

    Raises:
        TypeError: if the retrieved object is not a pipeline.
    """

    obj = _get_obj(ref)
    if not isinstance(obj, set) or any(not callable(o) for o in obj):
        msg = f"'{ref}' is not a pipeline"
        raise TypeError(msg)
    return obj  # ty: ignore[invalid-return-type]


def get_hook(ref: str) -> NodeHook:
    """Gets a hook based on its reference. The reference should be
    formatted ``{package}.{subpackage}.{...}:{name}``. Used to retrieve a
    hook based on a reference provided to the CLI.

    Args:
        ref: the hook reference

    Returns:
        the hook

    Raises:
        TypeError: if the retrieved object is not a hook.
    """

    obj = get_obj(ref)
    if not isinstance(obj, NodeHook):
        msg = f"'{ref}' is not a hook"
        raise TypeError(msg)
    return obj


def run_node_refs(
    node_refs: tuple[str, ...],
    hook_refs: tuple[str],
    *,
    save: SaveMode = "all",
) -> DataStoreType:
    """Runs nodes by their references. References should be formatted
    `{package}.{subpackage}.{...}:{object-name}`. This method should not be
    called directly by users.

    Args:
        node_refs: node references
        hook_refs: hook references
        save: save mode to run with, defaults to "all"

    Returns:
        RunReceipt

    """

    return run(
        *(get_node(ref) for ref in node_refs),
        hooks=[get_hook(ref) for ref in hook_refs],
        save=save,
    )


def run_pipeline_ref(
    pipeline_ref: str, hook_refs: tuple[str], *, save: SaveMode = "all"
) -> DataStoreType:
    """Runs a pipeline by its references. References should be formatted
    `{package}.{subpackage}.{...}:{object-name}`. This method should not be
    called directly by users.

    Args:
        pipeline_ref: pipeline reference
        hook_refs: hook references
        save: save mode to run with, defaults to "all"

    Returns:
        RunReceipt

    """

    return run(
        *get_pipeline(pipeline_ref),
        hooks=[get_hook(ref) for ref in hook_refs],
        save=save,
    )
