import logging
from collections.abc import Sequence
from itertools import chain
from types import ModuleType
from typing import Any, Literal, TypeAlias, TypeVar

from ordeq._fqn import AnyRef, ModuleName, ObjectRef
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._hook import NodeHook, RunHook, RunnerHook
from ordeq._io import IO, AnyIO, Input, _InputCache
from ordeq._nodes import Node, View
from ordeq._patch import _patch_nodes
from ordeq._process_nodes import NodeFilter
from ordeq._process_nodes_and_ios import process_nodes_and_ios
from ordeq._resolve import (
    Runnable,
    RunnableRef,
    _resolve_module_name_to_module,
    _resolve_refs_to_hooks,
)
from ordeq._substitute import (
    _resolve_refs_to_subs,
    _substitutes_modules_to_ios,
)

logger = logging.getLogger("ordeq.runner")

T = TypeVar("T")

# The save mode determines which outputs are saved. When set to:
# - 'all', all outputs are saved, including those of intermediate nodes.
# - 'sinks', only outputs of sink nodes are saved, i.e. those w/o successors.
# - 'none', to dry-run and save no outputs
# Future extension:
# - 'last', which saves the output of the last node for which no error
# occurred. This can be useful for debugging.
SaveMode: TypeAlias = Literal["all", "sinks", "none"]


def _load_inputs(inputs: Sequence[Input]) -> list[Any]:
    args = []
    for io in inputs:
        data = io.load()
        args.append(data)

        # TODO: optimize persisting only when needed
        if not io.is_persisted:
            io.persist(data)
    return args


def _save_outputs(outputs, values) -> None:
    for output, data in zip(outputs, values, strict=True):
        output.save(data)

        # TODO: optimize by persisting only when needed
        if isinstance(output, _InputCache):
            output.persist(data)


def _run_node_func(
    node: Node, args: list[Any], *, hooks: Sequence[NodeHook] = ()
) -> tuple[Any, ...]:
    logger.info("Running %s", node)

    try:
        values = node.func(*args)
    except Exception as exc:
        for node_hook in hooks:
            node_hook.on_node_call_error(node, exc)
        raise exc

    if len(node.outputs) == 0:
        values = ()
    elif len(node.outputs) == 1:
        values = (values,)
    else:
        values = tuple(values)

    return values


def _run_node(node: Node, hooks: Sequence[NodeHook] = ()) -> None:
    args = _load_inputs(node.inputs)
    results = _run_node_func(node, args=args, hooks=hooks)
    _save_outputs(node.outputs, results)


def _run_node_before_hooks(node, hooks) -> None:
    for node_hook in hooks:
        node_hook.before_node_run(node)


def _run_node_after_hooks(node, hooks) -> None:
    for node_hook in hooks:
        node_hook.after_node_run(node)


def _run_before_hooks(graph: NodeGraph, *, hooks: Sequence[RunHook]) -> None:
    for run_hook in hooks:
        run_hook.before_run(graph)


def _run_after_hooks(graph: NodeGraph, *, hooks: Sequence[RunHook]) -> None:
    for run_hook in hooks:
        run_hook.after_run(graph)


def _run_graph(
    graph: NodeGraph,
    *,
    node_hooks: Sequence[NodeHook] = (),
    run_hooks: Sequence[RunHook] = (),
) -> None:
    """Runs nodes in a graph topologically, ensuring IOs are loaded only once.

    Args:
        graph: node graph to run
        node_hooks: node hooks to execute
        run_hooks: run hooks to execute
    """

    _run_before_hooks(graph, hooks=run_hooks)

    for level in graph.topological_levels:
        for node in level:
            _run_node_before_hooks(node, hooks=node_hooks)
            _run_node(node, hooks=node_hooks)
            _run_node_after_hooks(node, hooks=node_hooks)

    # unpersist IO objects
    # TODO: optimize by unpersisting as soon as possible
    for gnode in graph.edges:
        io_objs = chain(gnode.inputs, gnode.outputs)
        for io_obj in io_objs:
            if isinstance(io_obj, _InputCache):
                io_obj.unpersist()

    _run_after_hooks(graph, hooks=run_hooks)


def run(
    *runnables: Runnable | RunnableRef,
    hooks: Sequence[RunnerHook | ObjectRef] = (),
    save: SaveMode = "all",
    verbose: bool = False,
    io: dict[AnyRef | AnyIO | ModuleType, AnyRef | AnyIO | ModuleType]
    | None = None,
    node_filter: NodeFilter | None = None,
    context: ModuleType | ModuleName | None = None,
) -> None:
    """Runs nodes in topological order.

    Args:
        runnables: Nodes to run, or modules or packages containing nodes.
        hooks: Run or node hooks to apply. Input and output hooks are taken
            from the IOs.
        save: One of `{"all", "sinks"}`. When set to "sinks", only saves the
            sink outputs. Defaults to "all".
        verbose: Whether to print the node graph.
        io: Mapping of IO objects to their run-time substitutes.
        node_filter: Method to filter nodes.
        context: Module to use as context for resolving string references.

    Arguments `runnables`, `hooks` and `io` also support string references.
    Each string reference should be formatted `module.submodule.[...]`
    (for modules) or `module.submodule.[...]:name` (for nodes, hooks and IOs).

    Examples:

    Run a single node:

    ```pycon
    >>> from pipeline import node
    >>> run(node)
    >>> # or, equivalently:
    >>> run("pipeline:node")
    ```

    Run more than one node:

    ```pycon
    >>> from pipeline import node_a, node_b
    >>> run(node_a, node_b)
    >>> # or, equivalently:
    >>> run("pipeline:node_a", "pipeline:node_b")
    ```

    Run an entire pipeline:

    ```pycon
    >>> import pipeline # a single module, or a package containing nodes
    >>> run(pipeline)
    >>> # or, equivalently:
    >>> run("pipeline")
    ```

    Run a single node with a hook:

    ```pycon
    >>> from hooks import my_hook
    >>> run(node, hooks=[my_hook])
    >>> # or, equivalently:
    >>> run(node, hooks=["hooks:my_hook"])
    ```

    Run a single node with alternative IO:
    (this example substitutes `output` with an instance of `Print`)

    ```pycon
    >>> from pipeline import output  # an IO used by the pipeline
    >>> from ordeq_common import Print
    >>> run(node, io={output: Print()})
    ```

    Run a pipeline with an alternative catalog:

    ```pycon
    >>> import pipeline
    >>> from catalogs import base, local
    >>> run(pipeline, io={base: local})
    >>> # or, equivalently:
    >>> run(pipeline, io={"catalogs.base": "catalogs.local"})
    ```

    Run without saving intermediate IOs:

    ```pycon
    >>> import pipeline
    >>> run(pipeline, save="sinks")
    ```

    Run nodes a filtered subset of nodes in `pipeline`:

    ```pycon
    >>> from ordeq import Node
    >>> import pipeline
    >>> def filter_daily_frequency(node: Node) -> bool:
    ...     # Filters the nodes with attribute "frequency" set to daily
    ...     # e.g.: @node(..., frequency="daily")
    ...     return node.attributes.get("frequency", None) == "daily"
    >>> run(pipeline, filter=filter_daily_frequency)

    ```

    """
    resolved_context = (
        _resolve_module_name_to_module(context) if context else None
    )
    resolved_run_hooks, resolved_node_hooks = _resolve_refs_to_hooks(*hooks)
    resolved_subs = _resolve_refs_to_subs(io or {})

    nodes = process_nodes_and_ios(
        *runnables,
        context=[resolved_context] if resolved_context else [],
        node_filter=node_filter,
    )
    graph = NodeGraph.from_nodes(nodes)

    save_mode_patches: dict[AnyIO, AnyIO] = {}
    if save in {"none", "sinks"}:
        # Replace relevant outputs with ordeq.IO, that does not save
        save_nodes = (
            nodes
            if save == "none"
            else [node for node in nodes if node not in graph.sinks]
        )
        for node in save_nodes:
            if not isinstance(node, View):
                for output in node.outputs:
                    save_mode_patches[output] = IO()

    user_patches = _substitutes_modules_to_ios(resolved_subs)
    patches = {**user_patches, **save_mode_patches}
    if patches:
        patched_nodes = _patch_nodes(*nodes, patches=patches)
        graph = NodeGraph.from_nodes(patched_nodes)

    if verbose:
        graph_with_io = NodeIOGraph.from_graph(graph)
        print(graph_with_io)

    _run_graph(
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
    )
