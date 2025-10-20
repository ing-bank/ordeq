from pathlib import Path
from types import ModuleType
from typing import Any, overload

from ordeq._resolve import _resolve_runnables_to_nodes_and_ios  # noqa: PLC2701

from ordeq_manifest.models import ProjectModel


@overload
def create_manifest_json(
    package: ModuleType,
    output: None = None,
    indent: int = 2,
    **json_options: Any,
) -> str: ...


@overload
def create_manifest_json(
    package: ModuleType, output: Path, indent: int = 2, **json_options: Any
) -> None: ...


def create_manifest_json(
    package: ModuleType,
    output: Path | None = None,
    indent: int = 2,
    **json_options: Any,
) -> str | None:
    """Creates a JSON manifest for the given package or module.

    Args:
        package: The package or module to create a manifest for.
        indent: The number of spaces to use for indentation in the JSON output.
        output: path to the JSON file. Will be created if it does not exist.
        **json_options: Additional options to pass to the `model_dump_json`
            method.

    Returns:
        str: The JSON manifest of the package or module.

    """

    project_model = create_manifest(package)
    json = project_model.model_dump_json(indent=indent, **json_options)
    if output:
        output.write_text(data=json, encoding="utf-8")
        return None
    return json


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
