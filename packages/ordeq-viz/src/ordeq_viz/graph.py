from ordeq._resolve import Catalog, Pipeline
from ordeq_manifest.models import IOModel, NodeModel, ProjectModel


def _gather_graph(
    nodes: Pipeline, ios: Catalog
) -> tuple[dict[str, NodeModel], dict[str, IOModel]]:
    """Build a graph of nodes and datasets from pipeline (set of nodes)

    Args:
        nodes: nodes
        ios: ios

    Returns:
        metadata for nodes (NodeData)
        metadata for ios (IOData)
    """
    project = ProjectModel.from_nodes_and_ios("__default__", nodes, ios)
    return project.nodes, project.ios
