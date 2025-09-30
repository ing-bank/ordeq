from typing import Any

from ordeq.framework.io import Input, Output
from ordeq.framework.nodes import Node

from ordeq_viz.graph import _gather_graph


def _filter_none(d: dict[str, Any]) -> dict[str, Any]:
    return {
        k: (_filter_none(v) if isinstance(v, dict) else v)
        for k, v in d.items()
        if (v is not None if not isinstance(v, dict) else _filter_none(v))
    }


def _make_mermaid_header(
    header_dict: dict[str, str | dict[str, str | None] | None],
) -> str:
    """Generate the mermaid header.

    Args:
        header_dict: A dictionary containing header fields.

    Returns:
        The mermaid header as a string.
    """

    header_dict = _filter_none(header_dict)

    if not header_dict:
        return ""

    header_lines = ["---"]
    for key, value in header_dict.items():
        if isinstance(value, dict):
            header_lines.append(f"{key}:")
            for subkey, subvalue in value.items():
                header_lines.append(f"  {subkey}: {subvalue}")
        else:
            header_lines.append(f'{key}: "{value}"')
    header_lines.append("---")
    return "\n".join(header_lines) + "\n"


def pipeline_to_mermaid(
    nodes: set[Node],
    datasets: dict[str, Input | Output],
    legend: bool = True,
    use_dataset_styles: bool = True,
    connect_wrapped_datasets: bool = True,
    title: str | None = None,
    layout: str | None = None,
    theme: str | None = None,
    look: str | None = None,
) -> str:
    """Convert a pipeline to a mermaid diagram

    Args:
        nodes: set of `ordeq.framework.Node`
        datasets: dict of name and `ordeq.framework.IO`
        legend: if True, display a legend
        use_dataset_styles: if True, use a distinct color for each dataset type
        connect_wrapped_datasets: if True, connect wrapped datasets with a
            dashed line
        title: Title of the mermaid diagram
        layout: Layout type for the diagram (e.g., 'dagre')
        theme: Theme for the diagram (e.g., 'neo')
        look: Look and feel for the diagram (e.g., 'neo')

    Returns:
        the pipeline rendered as mermaid diagram syntax

    Examples:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_viz import (
    ...    gather_ios_from_module,
    ...    gather_nodes_from_registry,
    ...    pipeline_to_mermaid
    ... )

    >>> import catalog as catalog_module  # doctest: +SKIP
    >>> import pipeline as pipeline_module  # doctest: +SKIP

    ```

    Gather all nodes in your project:
    ```python
    >>> nodes = gather_nodes_from_registry()

    ```

    Find all objects of type "IO" in catalog.py:
    ```python
    >>> datasets = gather_ios_from_module(catalog_module)  # doctest: +SKIP
    >>> mermaid = pipeline_to_mermaid(nodes, datasets)  # doctest: +SKIP
    >>> Path("pipeline.mermaid").write_text(mermaid)  # doctest: +SKIP

    ```
    """

    header_dict = {
        "title": title,
        "config": {"layout": layout, "theme": theme, "look": look},
    }
    mermaid_header = _make_mermaid_header(header_dict)

    node_data, dataset_data = _gather_graph(nodes, datasets)

    wraps_data: list[tuple[int, str, int]] = []
    if connect_wrapped_datasets:
        for dataset in dataset_data:
            dataset_ = dataset.dataset
            for attribute, values in dataset_.references.items():
                wraps_data.extend(
                    (hash(value), attribute, hash(dataset_))
                    for value in values
                )

    node_style = "fill:#008AD7,color:#FFF"
    dataset_style = "fill:#FFD43B"
    dataset_styles = (
        "fill:#66c2a5",
        "fill:#fc8d62",
        "fill:#8da0cb",
        "fill:#e78ac3",
        "fill:#a6d854",
        "fill:#ffd92f",
        "fill:#e5c494",
        "fill:#b3b3b3",
        "fill:#ff69b4",
        "fill:#ff4500",
        "fill:#00ced1",
        "fill:#9370db",
        "fill:#ffa500",
        "fill:#20b2aa",
        "fill:#ff6347",
        "fill:#4682b4",
    )

    distinct_dataset_types = sorted({dataset.type for dataset in dataset_data})
    dataset_type_to_id = {
        dataset_type: idx
        for idx, dataset_type in enumerate(distinct_dataset_types)
    }

    data = mermaid_header
    data += """graph TB\n"""
    data += f"\tclassDef function {node_style}\n"
    data += f"\tclassDef dataset {dataset_style}\n"
    if use_dataset_styles:
        for idx in dataset_type_to_id.values():
            data += f"\tclassDef dataset{idx} {dataset_styles[idx]}\n"

    if legend:
        data += "\tsubgraph Legend\n"
        direction = "TB" if use_dataset_styles else "LR"
        data += f"\t\tdirection {direction}\n"
        if use_dataset_styles:
            data += "\t\tsubgraph Objects\n"
        data += "\t\t\tL0([Node]):::function\n"
        data += "\t\t\tL1[(IO)]:::dataset\n"
        if use_dataset_styles:
            data += "\t\tend\n"
            data += "\t\tsubgraph IO Types\n"
            for dataset_type, idx in dataset_type_to_id.items():
                data += f"\t\t\tL0{idx}[({dataset_type})]:::dataset{idx}\n"
            data += "\t\tend\n"
        data += "\tend\n"
        data += "\n"

    # Edges
    # Inputs/Outputs
    for node in node_data:
        for dataset_id in node.inputs:
            data += f"\t{dataset_id} --> {node.id}([{node.name}])\n"

        for dataset_id in node.outputs:
            data += f"\t{node.id}([{node.name}]) --> {dataset_id}\n"

    # Wrappers
    if connect_wrapped_datasets:
        for dataset_from_id, attr, dataset_to_id in wraps_data:
            data += f"\t{dataset_from_id} -.->|{attr}| {dataset_to_id}\n"

    # Nodes
    indent = 1
    tabs = "\t" * indent
    data += f'{tabs}subgraph pipeline["Pipeline"]\n'
    data += f"{tabs}\tdirection TB\n"
    for node in node_data:
        data += f"{tabs}\t{node.id}:::function\n"

    for dataset in dataset_data:
        if use_dataset_styles:
            class_name = f"dataset{dataset_type_to_id[dataset.type]}"
        else:
            class_name = "dataset"
        data += f"{tabs}\t{dataset.id}[({dataset.name})]:::{class_name}\n"

    data += f"{tabs}end\n"
    data += "\n"
    return data
