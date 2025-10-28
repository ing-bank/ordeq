import html
from itertools import cycle
from typing import Any

from ordeq._resolve import Catalog, Pipeline

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


def _hash_to_str(obj_id: int, io_names: dict[int, str]) -> str:
    if obj_id not in io_names:
        io_names[obj_id] = f"IO{len(io_names)}"
    return io_names[obj_id]


def pipeline_to_mermaid(
    nodes: Pipeline,
    ios: Catalog,
    legend: bool = True,
    use_dataset_styles: bool = True,
    # connect_wrapped_datasets: bool = True,
    title: str | None = None,
    layout: str | None = None,
    theme: str | None = None,
    look: str | None = None,
    io_shape_template: str = '[("{value}")]',
    node_shape_template: str = '(["{value}"])',
) -> str:
    """Convert a pipeline to a mermaid diagram

    Args:
        nodes: set of `ordeq.Node`
        ios: dict of name and `ordeq.IO`
        legend: if True, display a legend
        use_dataset_styles: if True, use a distinct color for each dataset type
        connect_wrapped_datasets: if True, connect wrapped datasets with a
            dashed line
        title: Title of the mermaid diagram
        layout: Layout type for the diagram (e.g., 'dagre')
        theme: Theme for the diagram (e.g., 'neo')
        look: Look and feel for the diagram (e.g., 'neo')
        io_shape_template: Shape template for IO nodes, with `{value}` as
            placeholder for the name
        node_shape_template: Shape template for processing nodes, with
            `{value}` as placeholder for the name

    Returns:
        the pipeline rendered as mermaid diagram syntax

    ```
    """
    io_names: dict[int, str] = {}
    # TODO: move to viz
    node_data, io_data = _gather_graph(nodes, ios)

    distinct_io_types = sorted({io.type for io in io_data.values()})
    distinct_io_types = {io_type: io_type.split(":")[1] for io_type in distinct_io_types}

    # wraps_data: list[tuple[int, str, int]] = []
    # if connect_wrapped_datasets:
    #     for dataset in io_data:
    #         dataset_ = dataset.dataset
    #         for attribute, values in dataset_.references.items():
    #             wraps_data.extend(
    #                 (hash(value), attribute, hash(dataset_))
    #                 for value in values
    #             )

    header_dict = {
        "title": title,
        "config": {"layout": layout, "theme": theme, "look": look},
    }

    # Styles
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

    classes = {"node": node_style, "io": dataset_style}

    mermaid_header = _make_mermaid_header(header_dict)

    io_classes = {}
    if use_dataset_styles:
        for (idx, ids), style in zip(
            enumerate(distinct_io_types), cycle(dataset_styles), strict=False
        ):
            io_classes[ids] = f"io{idx}"
            classes[f"io{idx}"] = style

    # Rendering
    data = mermaid_header
    data += """graph TB\n"""

    if legend:
        data += '\tsubgraph legend["Legend"]\n'
        direction = "TB" if use_dataset_styles else "LR"
        data += f"\t\tdirection {direction}\n"
        if use_dataset_styles:
            data += "\t\tsubgraph objects[\"Objects\"]\n"
        data += f"\t\t\tL0{node_shape_template.format(value='Node')}:::node\n"
        data += f"\t\t\tL1{io_shape_template.format(value='IO')}:::io\n"
        if use_dataset_styles:
            data += "\t\tend\n"
            data += "\t\tsubgraph io_types[\"IO Types\"]\n"
            for idx, dataset_type in distinct_io_types.items():
                data += (
                    f"\t\t\t{idx}{io_shape_template.format(value=dataset_type)}"
                    f":::{io_classes[idx]}\n"
                )
            data += "\t\tend\n"
        data += "\tend\n"
        data += "\n"

    # Edges
    # Inputs/Outputs
    for node in node_data.values():
        for dataset_id in node.inputs:
            data += f"\t{dataset_id} --> {node.id}\n"

        for dataset_id in node.outputs:
            data += f"\t{node.id} --> {dataset_id}\n"

    data += "\n"

    # Wrappers
    # if connect_wrapped_datasets:
    #     for dataset_from_id, attr, dataset_to_id in wraps_data:
    #         data += (
    #             f"\t{_hash_to_str(dataset_from_id, io_names)} -.->|{attr}| "
    #             f"{_hash_to_str(dataset_to_id, io_names)}\n"
    #         )

    # Nodes
    indent = 1
    tabs = "\t" * indent
    data += f'{tabs}subgraph pipeline["Pipeline"]\n'
    data += f"{tabs}\tdirection TB\n"
    for node in node_data.values():
        data += (
            f"{tabs}\t{node.id}"
            f"{node_shape_template.format(value=html.escape(node.name))}"
            f":::node\n"
        )

    for io in io_data.values():
        class_name = io_classes[io.type] if use_dataset_styles else "io"
        data += (
            f"{tabs}\t{io.id}"
            f"{io_shape_template.format(value=html.escape(io.name))}"
            f":::{class_name}\n"
        )

    data += f"{tabs}end\n"
    data += "\n"

    # Classes
    for class_name, style in classes.items():
        data += f"\tclassDef {class_name} {style}\n"

    return data
