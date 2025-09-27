from types import ModuleType

from ordeq_manifest._gather import gather
from ordeq_manifest.models import ProjectModel


def create_manifest_json(package: ModuleType) -> str:
    """Creates a JSON manifest for the given package or module.

    Args:
        package: The package or module to create a manifest for.

    Returns:
        str: The JSON manifest of the package or module.

    """

    project_model = create_manifest(package)
    return project_model.model_dump_json(indent=1)


def create_manifest(package: ModuleType) -> ProjectModel:
    """Creates an in-memory manifest for the given package or module.

    Args:
        package: The package or module to create the manifest for.

    Returns:
        ProjectModel: the manifest of the package or module.
    """

    name = package.__name__
    nodes, ios = gather(package)
    return ProjectModel(name=name, nodes=nodes, ios=ios)
