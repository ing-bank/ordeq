from types import ModuleType
from typing import Any

from ordeq._resolve import _resolve_runnables_to_nodes_and_ios  # noqa: PLC2701

from ordeq_manifest.models import ProjectModel


def create_manifest_json(
    package: ModuleType, indent: int = 2, **json_options: Any
) -> str:
    """Creates a JSON manifest for the given package or module.

    Args:
        package: The package or module to create a manifest for.
        indent: The number of spaces to use for indentation in the JSON output.
        **json_options: Additional options to pass to the `model_dump_json`
            method.

    Returns:
        str: The JSON manifest of the package or module.

    """

    project_model = create_manifest(package)
    return project_model.model_dump_json(indent=indent, **json_options)


def create_manifest(package: ModuleType) -> ProjectModel:
    """Creates an in-memory manifest for the given package or module.

    Args:
        package: The package or module to create the manifest for.

    Returns:
        ProjectModel: the manifest of the package or module.
    """

    name = package.__name__
    nodes, ios = _resolve_runnables_to_nodes_and_ios(package)
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
