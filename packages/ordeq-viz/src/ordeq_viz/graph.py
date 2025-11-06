import operator
from dataclasses import dataclass, field
from typing import Any

from ordeq import Node
from ordeq._graph import NodeGraph, NodeIOGraph  # noqa: PLC2701 private import
from ordeq._io import AnyIO
from ordeq._resolve import Catalog


@dataclass
class NodeData:
    id: int | str
    node: Node
    name: str
    inputs: list[int]
    outputs: list[int]
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class IOData:
    id: int
    dataset: AnyIO
    name: str
    type: str
    attributes: dict[str, Any] = field(default_factory=dict)


def _add_io_data(dataset, reverse_lookup, io_data) -> int:
    """Add IOData for a dataset to the io_data dictionary.

    Args:
        dataset: the dataset (Input or Output)
        reverse_lookup: a dictionary mapping dataset IDs to names
        io_data: a dictionary to store IOData objects

    Returns:
        The ID of the dataset in the io_data dictionary.
    """
    dataset_id = hash(dataset)
    if dataset_id not in io_data:
        io_data[dataset_id] = IOData(
            id=dataset_id,
            dataset=dataset,
            name=reverse_lookup[dataset_id],
            type=dataset.__class__.__name__,
        )

    # Handle wrapped datasets
    for wrapped_attribute in dataset.references.values():
        for wrapped_dataset in wrapped_attribute:
            wrapped_id = hash(wrapped_dataset)
            if wrapped_id not in io_data:
                try:
                    name = reverse_lookup[wrapped_id]
                except KeyError:
                    name = "<anonymous>"

                io_data[wrapped_id] = IOData(
                    id=wrapped_id,
                    dataset=wrapped_dataset,
                    name=name,
                    type=wrapped_dataset.__class__.__name__,
                )
    return dataset_id


def _gather_graph(
    nodes: set[Node], ios: Catalog
) -> tuple[list[NodeData], list[IOData]]:
    """Build a graph of nodes and datasets from pipeline (set of nodes)

    Args:
        nodes: nodes
        ios: ios

    Returns:
        metadata for nodes (NodeData)
        metadata for ios (IOData)
    """
    graph = NodeIOGraph.from_nodes(nodes)

    reverse_lookup = {
        hash(io): name
        for _, named_io in sorted(ios.items(), key=operator.itemgetter(0))
        for name, io in sorted(named_io.items(), key=operator.itemgetter(0))
    }

    for io in graph.ios:
        io_id = hash(io)
        if io_id not in reverse_lookup:
            reverse_lookup[io_id] = "<anonymous>"

    nodes_ = []
    io_data: dict[int, IOData] = {}

    ordering = NodeGraph.from_graph(graph).topological_ordering

    for line in ordering:
        inputs = [
            _add_io_data(input_dataset, reverse_lookup, io_data)
            for input_dataset in line.inputs
        ]
        outputs = [
            _add_io_data(output_dataset, reverse_lookup, io_data)
            for output_dataset in line.outputs
        ]
        nodes_.append(
            NodeData(
                id=line.func.__name__,
                node=line,
                name=line.func.__name__,
                inputs=inputs,
                outputs=outputs,
            )
        )

    return nodes_, list(io_data.values())
