## Resource

```python
import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(ordeq_dev_tools))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))

```

## Output

```text
ordeq_dev_tools {}
ordeq_dev_tools.__main__ {'Path': 'pathlib', 'Final': 'typing', 'run': 'ordeq'}
ordeq_dev_tools.ios {}
ordeq_dev_tools.ios.github_release {'dataclass': 'dataclasses', 'Output': 'ordeq', 'Literal': 'typing', 'run_command': 'ordeq_dev_tools.utils'}
ordeq_dev_tools.paths {'Path': 'pathlib'}
ordeq_dev_tools.pipelines {}
ordeq_dev_tools.pipelines.docs_package_overview {'Path': 'pathlib', 'Generator': 'collections.abc', 'node': 'ordeq', 'ROOT_PATH': 'ordeq_dev_tools.paths', 'PACKAGES_PATH': 'ordeq_dev_tools.paths', 'packages': 'ordeq_dev_tools.pipelines.shared', 'TextLinesStream': 'ordeq_files', 'TOML': 'ordeq_toml'}
ordeq_dev_tools.pipelines.docs_update_just {'node': 'ordeq', 'run': 'ordeq', 'Text': 'ordeq_files', 'ROOT_PATH': 'ordeq_dev_tools.paths', 'run_command': 'ordeq_dev_tools.utils'}
ordeq_dev_tools.pipelines.generate_draft_releases {'node': 'ordeq', 'run': 'ordeq', 'pipeline': 'ordeq', 'GithubRelease': 'ordeq_dev_tools.ios.github_release', 'generate_release_notes': 'ordeq_dev_tools.pipelines', 'packages': 'ordeq_dev_tools.pipelines.shared', 'run_command': 'ordeq_dev_tools.utils'}
ordeq_dev_tools.pipelines.generate_release_notes {'Any': 'typing', 'node': 'ordeq', 'Input': 'ordeq', 'IO': 'ordeq', 'Version': 'packaging.version', 'run_command': 'ordeq_dev_tools.utils'}
ordeq_dev_tools.pipelines.list_changed_packages {'Path': 'pathlib', 'node': 'ordeq', 'JSON': 'ordeq_files', 'DATA_PATH': 'ordeq_dev_tools.paths', 'run_command': 'ordeq_dev_tools.utils'}
ordeq_dev_tools.pipelines.list_dependencies {'Any': 'typing', 'node': 'ordeq', 'JSON': 'ordeq_files', 'Text': 'ordeq_files', 'TOML': 'ordeq_toml', 'DATA_PATH': 'ordeq_dev_tools.paths', 'ROOT_PATH': 'ordeq_dev_tools.paths'}
ordeq_dev_tools.pipelines.relevant_packages {'Any': 'typing', 'node': 'ordeq', 'JSON': 'ordeq_files', 'DATA_PATH': 'ordeq_dev_tools.paths'}
ordeq_dev_tools.pipelines.shared {'node': 'ordeq', 'PACKAGES_PATH': 'ordeq_dev_tools.paths'}
ordeq_dev_tools.pipelines.validate_pyproject {'Path': 'pathlib', 'node': 'ordeq', 'ROOT_PATH': 'ordeq_dev_tools.paths', 'PACKAGES_PATH': 'ordeq_dev_tools.paths', 'packages': 'ordeq_dev_tools.pipelines.shared', 'TOML': 'ordeq_toml'}
ordeq_dev_tools.pipelines.viz_self {'node': 'ordeq', 'Text': 'ordeq_files', 'viz': 'ordeq_viz', 'DATA_PATH': 'ordeq_dev_tools.paths'}
ordeq_dev_tools.utils {'ROOT_PATH': 'ordeq_dev_tools.paths'}

```