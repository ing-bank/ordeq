import logging
from collections.abc import Callable, Sequence
from itertools import chain
from types import ModuleType
from typing import Literal, TypeAlias, TypeVar, cast

from ordeq._fqn import AnyRef, ObjectRef, object_ref_to_fqn
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._hook import NodeHook, RunHook, RunnerHook
from ordeq._io import IO, AnyIO, Input, _InputCache
from ordeq._nodes import Node, View
from ordeq._resolve import _resolve_refs_to_hooks, _resolve_runnables_to_nodes
from ordeq._substitute import (
    _resolve_refs_to_subs,
    _substitutes_modules_to_ios,
)

logger = logging.getLogger("ordeq.runner")

T = TypeVar("T")

Runnable: TypeAlias = ModuleType | Callable | str
# The save mode determines which outputs are saved. When set to:
# - 'all', all outputs are saved, including those of intermediate nodes.
# - 'sinks', only outputs of sink nodes are saved, i.e. those w/o successors.
# - 'none', to dry-run and save no outputs
# Future extension:
# - 'last', which saves the output of the last node for which no error
# occurred. This can be useful for debugging.
SaveMode: TypeAlias = Literal["all", "sinks", "none"]


def _run_node(node: Node, *, hooks: Sequence[NodeHook] = ()) -> None:
    for node_hook in hooks:
        node_hook.before_node_run(node)

    args = []
    for input_dataset in node.inputs:
        # We know at this point that all view inputs are patched by
        # sentinel IOs, so we can safely cast here.
        data = cast("Input", input_dataset).load()
        args.append(data)
        if isinstance(input_dataset, _InputCache):
            input_dataset.persist(data)

    module_name, node_name = object_ref_to_fqn(node.name)
    node_type = "view" if isinstance(node, View) else "node"
    logger.info(
        'Running %s "%s" in module "%s"', node_type, node_name, module_name
    )

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

    # saving computed data
    for output, data in zip(node.outputs, values, strict=True):
        output.save(data)

        # persisting computed data only if outputs are loaded again later
        if isinstance(output, _InputCache):
            output.persist(data)

    for node_hook in hooks:
        node_hook.after_node_run(node)


def _run_graph(graph: NodeGraph, *, hooks: Sequence[NodeHook] = ()) -> None:
    """Runs nodes in a graph topologically, ensuring IOs are loaded only once.

    Args:
        graph: node graph to run
        hooks: hooks to apply
    """

    for level in graph.topological_levels:
        for node in level:
            _run_node(node, hooks=hooks)

    # unpersist IO objects
    for gnode in graph.nodes:
        io_objs = chain(gnode.inputs, gnode.outputs)
        for io_obj in io_objs:
            if isinstance(io_obj, _InputCache):
                io_obj.unpersist()


def _run_before_hooks(graph: NodeGraph, *, hooks: Sequence[RunHook]) -> None:
    for run_hook in hooks:
        run_hook.before_run(graph)


def _run_after_hooks(graph: NodeGraph, *, hooks: Sequence[RunHook]) -> None:
    for run_hook in hooks:
        run_hook.after_run(graph)


def run(
    *runnables: Runnable,
    hooks: Sequence[RunnerHook | ObjectRef] = (),
    save: SaveMode = "all",
    verbose: bool = False,
    io: dict[AnyRef | AnyIO | ModuleType, AnyRef | AnyIO | ModuleType]
    | None = None,
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

    """

    nodes = _resolve_runnables_to_nodes(*runnables)
    io_subs = _resolve_refs_to_subs(io or {})
    patches = _substitutes_modules_to_ios(io_subs)

    if save in {"none", "sinks"}:
        # Replace relevant outputs with ordeq.IO, that does not save
        save_nodes = (
            nodes
            if save == "none"
            # This builds the graph twice, can be optimized.
            else [
                node
                for node in nodes
                if node
                not in NodeGraph.from_graph(
                    NodeIOGraph.from_nodes(nodes, patches=patches)  # type: ignore[arg-type]
                ).sink_nodes
            ]
        )
        for node in save_nodes:
            for output in node.outputs:
                patches[output] = IO()

    graph_with_io = NodeIOGraph.from_nodes(nodes, patches=patches)  # type: ignore[arg-type]

    if verbose:
        print(graph_with_io)

    graph = NodeGraph.from_graph(graph_with_io)

    # Validate nodes
    for node in graph.topological_ordering:
        node.validate()

    run_hooks, node_hooks = _resolve_refs_to_hooks(*hooks)

    _run_before_hooks(graph, hooks=run_hooks)
    _run_graph(graph, hooks=node_hooks)
    _run_after_hooks(graph, hooks=run_hooks)
