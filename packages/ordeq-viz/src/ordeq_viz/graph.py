from dataclasses import dataclass, field
from typing import Any

from ordeq import Input, IOException, Node, Output
from ordeq.graph import NodeGraph


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
    dataset: Input | Output
    name: str
    type: str
    attributes: dict[str, Any] = field(default_factory=dict)


def _add_io_data(dataset, reverse_lookup, io_data, kind):
    """Add IOData for a dataset to the io_data dictionary.

    Args:
        dataset: the dataset (Input or Output)
        reverse_lookup: a dictionary mapping dataset IDs to names
        io_data: a dictionary to store IOData objects
        kind: a string indicating whether the dataset is an Input or Output

    Returns:
        The ID of the dataset in the io_data dictionary.

    Raises:
        IOException: when inputs or outputs from any of the nodes is missing
            in the "datasets" variable
    """
    dataset_id = hash(dataset)
    if dataset_id not in io_data:
        try:
            io_data[dataset_id] = IOData(
                id=dataset_id,
                dataset=dataset,
                name=reverse_lookup[dataset_id],
                type=dataset.__class__.__name__,
            )
        except KeyError:
            raise IOException(
                f"{kind} dataset was not provided. Missing catalog entry "
                f"for {dataset}."
            ) from None

    # Handle wrapped datasets
    for wrapped_attribute in dataset.references.values():
        for wrapped_dataset in wrapped_attribute:
            wrapped_id = hash(wrapped_dataset)
            if wrapped_id not in io_data:
                try:
                    io_data[wrapped_id] = IOData(
                        id=wrapped_id,
                        dataset=wrapped_dataset,
                        name=reverse_lookup[wrapped_id],
                        type=wrapped_dataset.__class__.__name__,
                    )
                except KeyError:
                    raise IOException(
                        "Wrapped dataset was not provided. Missing catalog "
                        f"entry for {wrapped_dataset}."
                    ) from None
    return dataset_id


def _gather_graph(
    pipeline: set[Node], datasets: dict[str, Input | Output]
) -> tuple[list[NodeData], list[IOData]]:
    """Build a graph of nodes and datasets from pipeline (set of nodes)

    Args:
        pipeline: set of nodes
        datasets: dictionary from name to datasets

    Returns:
        metadata for nodes (NodeData)
        metadata for datasets (IOData)
    """
    reverse_lookup = {
        hash(dataset): name for name, dataset in datasets.items()
    }

    nodes = []
    io_data: dict[int, IOData] = {}

    ordering = NodeGraph.from_nodes(pipeline).topological_ordering

    for line in ordering:
        inputs = [
            _add_io_data(input_dataset, reverse_lookup, io_data, "Input")
            for input_dataset in line.inputs
        ]
        outputs = [
            _add_io_data(output_dataset, reverse_lookup, io_data, "Output")
            for output_dataset in line.outputs
        ]
        nodes.append(
            NodeData(
                id=line.func.__name__,
                node=line,
                name=line.func.__name__,
                inputs=inputs,
                outputs=outputs,
            )
        )

    return nodes, list(io_data.values())
