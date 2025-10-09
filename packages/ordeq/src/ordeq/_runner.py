import logging
from collections.abc import Callable, Sequence
from itertools import chain
from types import ModuleType
from typing import Literal, TypeVar

from ordeq._graph import NodeGraph
from ordeq._hook import NodeHook, RunHook
from ordeq._io import Input, Output, _InputCache
from ordeq._nodes import Node
from ordeq._resolve import _resolve_runnables_to_nodes

logger = logging.getLogger("ordeq.runner")

T = TypeVar("T")

DataStoreType = dict[Input[T] | Output[T], T]
# The save mode determines which outputs are saved. When set to:
# - 'all', all outputs are saved, including those of intermediate nodes.
# - 'sinks', only outputs of sink nodes are saved, i.e. those w/o successors.
# - 'none', to dry-run and save no outputs
# Future extension:
# - 'last', which saves the output of the last node for which no error
# occurred. This can be useful for debugging.
SaveMode = Literal["all", "sinks", "none"]


def _save_outputs(
    node: Node, values: Sequence[T], save: bool = True
) -> dict[Input[T] | Output[T], T]:
    computed: dict[Input[T] | Output[T], T] = {}
    for output_dataset, data in zip(node.outputs, values, strict=False):
        computed[output_dataset] = data

        # TODO: this can be handled in the `save_wrapper`
        if save:
            output_dataset.save(data)

    return computed


def _run_node(
    node: Node, *, hooks: Sequence[NodeHook] = (), save: bool = True
) -> DataStoreType:
    node.validate()

    for node_hook in hooks:
        node_hook.before_node_run(node)

    args = [input_dataset.load() for input_dataset in node.inputs]

    # persisting loaded data
    for node_input, data in zip(node.inputs, args, strict=True):
        if isinstance(node_input, _InputCache):
            node_input.persist(data)

    logger.info("Running node %s", node)

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

    computed = _save_outputs(node, values, save=save)

    # persisting computed data only if outputs are loaded again later
    for node_output in node.outputs:
        if isinstance(node_output, _InputCache):
            node_output.persist(computed[node_output])  # ty: ignore[call-non-callable]

    for node_hook in hooks:
        node_hook.after_node_run(node)

    return computed


def _run_graph(
    graph: NodeGraph,
    *,
    hooks: Sequence[NodeHook] = (),
    save: SaveMode = "all",
    io: dict[Input[T] | Output[T], Input[T] | Output[T]] | None = None,
) -> DataStoreType:
    """Runs nodes in a graph topologically, ensuring IOs are loaded only once.

    Args:
        graph: node graph to run
        hooks: hooks to apply
        hooks: hooks to apply
        save: 'all' | 'sinks' | 'none'.
            If 'sinks', only saves the outputs of sink nodes in the graph.
        io: mapping of IO objects to their replacements

    Returns:
        a dict mapping each IO to the computed data

    """

    patched_nodes: dict[Node, Node] = {}
    for node in graph.nodes:
        patched_nodes[node] = _patch_io(node, io or {})

    data_store: dict = {}  # For each IO, the loaded data

    # TODO: Create _Patch wrapper for IO?
    for node in graph.topological_ordering:
        if (save == "sinks" and node in graph.sink_nodes) or save == "all":
            save_node = True
        else:
            save_node = False

        computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)
        data_store.update(computed)

    reverse_io = {v: k for k, v in (io or {}).items()}
    patched_data_store = {}
    for k, v in data_store.items():
        patched_data_store[reverse_io.get(k, k)] = v

    # unpersist IO objects
    for gnode in graph.nodes:
        io_objs = chain(gnode.inputs, gnode.outputs)
        for io_obj in io_objs:
            if isinstance(io_obj, _InputCache):
                io_obj.unpersist()

    return patched_data_store


def _patch_io(
    node: Node, io: dict[Input[T] | Output[T], Input[T] | Output[T]]
) -> Node:
    """Patches the inputs and outputs of a node with the provided IO mapping.

    Args:
        node: the original node
        io: mapping of Input/Output objects to their replacements

    Returns:
        the node with patched inputs and outputs

    """

    return node._replace(
        inputs=[io.get(ip, ip) for ip in node.inputs],  # type: ignore[misc]
        outputs=[io.get(op, op) for op in node.outputs],  # type: ignore[misc]
    )


def run(
    *runnables: ModuleType | Callable | str,
    hooks: Sequence[NodeHook | RunHook] = (),
    save: SaveMode = "all",
    verbose: bool = False,
    io: dict[Input[T] | Output[T], Input[T] | Output[T]] | None = None,
) -> DataStoreType:
    """Runs nodes in topological order.

    Args:
        runnables: the nodes to run, or modules or packages containing nodes
        hooks: hooks to apply
        save: 'all' | 'sinks'. If 'sinks', only saves the sink outputs
        verbose: whether to print the node graph
        io: mapping of IO objects to their replacements

    Returns:
        a dict mapping each IO to the computed data

    """

    nodes = _resolve_runnables_to_nodes(*runnables)
    graph = NodeGraph.from_nodes(nodes)

    if verbose:
        print(graph)

    node_hooks: list[NodeHook] = [h for h in hooks if isinstance(h, NodeHook)]
    run_hooks: list[RunHook] = [h for h in hooks if isinstance(h, RunHook)]

    for run_hook in run_hooks:
        run_hook.before_run(graph)

    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

    for run_hook in run_hooks:
        run_hook.after_run(graph, result)

    return result
