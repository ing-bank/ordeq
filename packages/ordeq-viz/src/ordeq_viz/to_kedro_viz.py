import inspect
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from ordeq import Node
from ordeq._resolve import Catalog

from ordeq_viz.graph import IOData, NodeData, _gather_graph


@dataclass
class Task:
    id: str
    name: str
    tags: list[str]
    pipelines: list[str]
    modular_pipelines: list[str] | None
    parameters: dict
    type: str = "task"


@dataclass
class TaskDetails:
    code: str
    filepath: str
    parameters: dict
    run_command: str
    inputs: list[str]
    outputs: list[str]


@dataclass
class Data:
    id: str
    name: str
    tags: list[str]
    pipelines: list[str]
    modular_pipelines: list[str] | None
    layer: str | None
    dataset_type: str | None
    stats: None
    type: str = "data"


@dataclass
class DataDetails:
    type: str
    filepath: str = ""
    run_command: str = ""
    preview: None = None
    preview_type: str = "TablePreview"
    stats: None = None


@dataclass
class Edge:
    source: str
    target: str


@dataclass
class Pipeline:
    id: str
    name: str


@dataclass
class ModularPipeline:
    id: str
    name: str
    inputs: list[str]
    outputs: list[str]
    children: list[dict[str, str]]


@dataclass
class Main:
    nodes: list[Task | Data]
    edges: list[Edge]
    layers: list[str]
    tags: list[str]
    pipelines: list[Pipeline]
    modular_pipelines: dict[str, ModularPipeline]
    selected_pipeline: str


def _generate_nodes(nodes: list[NodeData], datasets: list[IOData]):
    x = {}
    for node in nodes:
        x[str(node.id)] = asdict(
            TaskDetails(
                code=node.attributes["source"],
                filepath=node.attributes["filepath"],
                parameters={},
                run_command="",
                inputs=[str(dataset_id) for dataset_id in node.inputs],
                outputs=[str(dataset_id) for dataset_id in node.outputs],
            )
        )

    for dataset in datasets:
        x[str(dataset.id)] = asdict(DataDetails(type=dataset.type))
    return x


def _generate_main(nodes: list[NodeData], datasets: list[IOData]):
    main_nodes = [
        Task(
            id=str(node.id),
            name=node.name,
            tags=[],
            pipelines=["__default__"],
            modular_pipelines=None,
            parameters={},
        )
        for node in nodes
    ] + [
        Data(
            id=str(dataset.id),
            name=dataset.name,
            tags=[],
            pipelines=["__default__"],
            modular_pipelines=None,
            layer=None,
            dataset_type=dataset.type,
            stats=None,
        )
        for dataset in datasets
    ]
    main = Main(
        nodes=main_nodes,
        edges=[
            Edge(source=str(dataset), target=str(node.id))
            for node in nodes
            for dataset in node.inputs
        ]
        + [
            Edge(source=str(node.id), target=str(dataset))
            for node in nodes
            for dataset in node.outputs
        ],
        layers=[],
        tags=[],
        pipelines=[Pipeline(id="__default__", name="__default__")],
        modular_pipelines={
            "__root__": ModularPipeline(
                id="__root__",
                name="__root__",
                inputs=[],
                outputs=[],
                children=[
                    {"id": node.id, "name": node.name} for node in main_nodes
                ],
            )
        },
        selected_pipeline="__default__",
    )
    return asdict(main)


def pipeline_to_kedro_viz(
    nodes: set[Node], ios: Catalog, output_directory: Path
) -> None:
    """Convert a pipeline to a kedro-viz static pipeline directory

    Run with:

    ```shell
    export KEDRO_DISABLE_TELEMETRY=true
    kedro viz run --load-file kedro-pipeline-example
    ```

    Args:
        nodes: set of `ordeq.Node`
        ios: dict of name and `ordeq.IO`
        output_directory: path to write the output data to

    Raises:
        FileExistsError: if the output directory already exists

    """
    node_data, dataset_data = _gather_graph(nodes, ios)

    # populate attributes for kedro-viz
    for node in node_data:
        node.attributes["source"] = inspect.getsource(node.node.func)
        node.attributes["filepath"] = node.node.func.__code__.co_filename

    if output_directory.exists():
        raise FileExistsError("Output directory already exists")

    (output_directory / "api").mkdir(parents=True)
    (output_directory / "api" / "nodes").mkdir()
    (output_directory / "api" / "pipelines").mkdir()

    main = _generate_main(node_data, dataset_data)
    main_data = json.dumps(main, indent=4)
    (output_directory / "api" / "main").write_text(main_data)
    (output_directory / "api" / "pipelines" / "__default__").write_text(
        main_data
    )

    data = _generate_nodes(node_data, dataset_data)
    for name, attributes in data.items():
        node_data_attributes = json.dumps(attributes, indent=4)
        (output_directory / "api" / "nodes" / name).write_text(
            node_data_attributes
        )
