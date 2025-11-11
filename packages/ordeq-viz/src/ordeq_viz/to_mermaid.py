import html
import logging
from collections import defaultdict
from itertools import cycle
from typing import Any

from ordeq import Node
from ordeq._resolve import Catalog

from ordeq_viz.graph import _gather_graph

logger = logging.getLogger(__name__)


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


def _hash_to_str(obj_id: int, io_names: dict[int, str]) -> str:
    if obj_id not in io_names:
        io_names[obj_id] = f"IO{len(io_names)}"
    return io_names[obj_id]


def pipeline_to_mermaid(
    nodes: set[Node],
    ios: Catalog,
    legend: bool = True,
    use_dataset_styles: bool = True,
    title: str | None = None,
    layout: str | None = None,
    theme: str | None = None,
    look: str | None = None,
    io_shape: str = "rect",
    node_shape: str = "rounded",
    view_shape: str = "subroutine",
    subgraphs: bool = False,
) -> str:
    """Convert a pipeline to a mermaid diagram

    Args:
        nodes: set of `ordeq.Node`
        ios: dict of name and `ordeq.IO`
        legend: if True, display a legend
        use_dataset_styles: if True, use a distinct color for each dataset type
        title: Title of the mermaid diagram
        layout: Layout type for the diagram (e.g., 'dagre')
        theme: Theme for the diagram (e.g., 'neo')
        look: Look and feel for the diagram (e.g., 'neo')
        io_shape: Shape for IO nodes in the diagram
        node_shape: Shape for processing nodes in the diagram
        view_shape: Shape for view nodes in the diagram
        subgraphs: if True, group nodes and IOs by their module in subgraphs

    Returns:
        the pipeline rendered as mermaid diagram syntax

    """
    if subgraphs:
        logger.warning(
            "Subgraphs are in pre-release, "
            "functionality may break in future releases "
            "without it being considered a breaking change."
        )
    io_names: dict[int, str] = {}

    node_modules, io_modules = _gather_graph(nodes, ios)

    node_data = [
        node
        for nodes_in_module in node_modules.values()
        for node in nodes_in_module
    ]
    dataset_data = [
        dataset
        for datasets_in_module in io_modules.values()
        for dataset in datasets_in_module
    ]
    views = [
        node
        for nodes_in_module in node_modules.values()
        for node in nodes_in_module
        if node.view
    ]
    io2view = {hash(view.outputs[0]): view for view in views}
    io_modules = {
        module: [ds for ds in datasets if hash(ds.id) not in io2view]
        for module, datasets in io_modules.items()
    }

    distinct_dataset_types = sorted({dataset.type for dataset in dataset_data})
    dataset_type_to_id = {
        dataset_type: idx
        for idx, dataset_type in enumerate(distinct_dataset_types)
    }

    header_dict = {
        "title": title,
        "config": {"layout": layout, "theme": theme, "look": look},
    }

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

    class_definitions = {}
    if node_data:
        class_definitions["node"] = "fill:#008AD7,color:#FFF"
    if dataset_data:
        class_definitions["io"] = "fill:#FFD43B"
    if views:
        class_definitions["view"] = "fill:#00C853,color:#FFF"

    class_assignments = defaultdict(list)

    mermaid_header = _make_mermaid_header(header_dict)

    if use_dataset_styles and dataset_data:
        for idx, style in zip(
            dataset_type_to_id.values(), cycle(dataset_styles), strict=False
        ):
            class_definitions[f"io{idx}"] = style

    data = mermaid_header
    data += """graph TB\n"""

    if legend and node_data:
        data += '\tsubgraph legend["Legend"]\n'
        data += "\t\tdirection TB\n"
        data += f'\t\tL0@{{shape: {node_shape}, label: "Node"}}\n'
        if views:
            data += f'\t\tL2@{{shape: {view_shape}, label: "View"}}\n'

        class_assignments["node"].append("L0")
        if views:
            class_assignments["view"].append("L2")

        if dataset_data:
            if not use_dataset_styles:
                data += f'\t\tL1@{{shape: {io_shape}, label: "IO"}}\n'
                class_assignments["io"].append("L1")
            else:
                for dataset_type, idx in dataset_type_to_id.items():
                    data += (
                        f"\t\tL0{idx}@{{shape: {io_shape}, "
                        f'label: "{dataset_type}"}}\n'
                    )
                    class_assignments[f"io{idx}"].append("L0" + str(idx))
        data += "\tend\n"
        data += "\n"

    # Edges
    # Inputs/Outputs
    for node in node_data:
        for dataset_id in node.inputs:
            if dataset_id in io2view:
                view_node = io2view[dataset_id]
                data += f"\t{view_node.id} --> {node.id}\n"
            else:
                data += (
                    f"\t{_hash_to_str(dataset_id, io_names)} --> {node.id}\n"
                )

        if not node.view:
            for dataset_id in node.outputs:
                data += (
                    f"\t{node.id} --> {_hash_to_str(dataset_id, io_names)}\n"
                )

    data += "\n"

    # Nodes
    indent = 2 if subgraphs else 1
    tabs = "\t" * indent

    for idx, (module, nodes_in_module) in enumerate(node_modules.items()):
        if subgraphs:
            data += f'\tsubgraph s{idx}["{module}"]\n'
            data += f"{tabs}direction TB\n"

        for node in nodes_in_module:
            shape = view_shape if node.view else node_shape
            data += (
                f"{tabs}{node.id}"
                f"@{{shape: {shape}, "
                f'label: "{html.escape(node.name)}"}}\n'
            )
            style = "node" if not node.view else "view"
            class_assignments[style].append(str(node.id))

        for io in sorted(
            io_modules.get(module, []),
            key=lambda io: _hash_to_str(io.id, io_names),
        ):
            if use_dataset_styles:
                class_assignments[f"io{dataset_type_to_id[io.type]}"].append(
                    _hash_to_str(io.id, io_names)
                )
            else:
                class_assignments["io"].append(_hash_to_str(io.id, io_names))

            data += (
                f"{tabs}{_hash_to_str(io.id, io_names)}"
                f'@{{shape: {io_shape}, label: "{html.escape(io.name)}"}}\n'
            )
        if subgraphs:
            data += "\tend\n"

    for io in sorted(
        io_modules.get(None, []), key=lambda io: _hash_to_str(io.id, io_names)
    ):
        if use_dataset_styles:
            class_assignments[f"io{dataset_type_to_id[io.type]}"].append(
                _hash_to_str(io.id, io_names)
            )
        else:
            class_assignments["io"].append(_hash_to_str(io.id, io_names))

        data += (
            f"\t{_hash_to_str(io.id, io_names)}"
            f'@{{shape: {io_shape}, label: "{html.escape(io.name)}"}}\n'
        )

    data += "\n"

    # Class assignments
    for class_name, ids in class_assignments.items():
        data += f"\tclass {','.join(ids)} {class_name}\n"

    # Class definitions
    for class_name, style in class_definitions.items():
        data += f"\tclassDef {class_name} {style}\n"

    return data
