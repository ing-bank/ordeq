## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(ordeq_dev_tools)
pprint(ios)

```

## Output

```text
{'ordeq_dev_tools.pipelines.docs_package_overview': {'package_overview': TextLinesStream(path=Path('/docs/packages.md'))},
 'ordeq_dev_tools.pipelines.docs_update_just': {'contribution_guide': Text(path=Path('/docs/CONTRIBUTING.md')),
                                                'docs_file': Text(path=Path('/docs/CONTRIBUTING.md')),
                                                'updated_docs_file': Text(path=Path('/docs/CONTRIBUTING.md'))},
 'ordeq_dev_tools.pipelines.generate_release_notes': {'new_tag': IO(idx=ID1),
                                                      'package': Input(idx=ID2),
                                                      'release_notes': IO(idx=ID3)},
 'ordeq_dev_tools.pipelines.list_changed_packages': {'changed_packages': JSON(path=Path('/data/dev_tools/changed_packages.json'))},
 'ordeq_dev_tools.pipelines.list_dependencies': {'affected_dependencies': JSON(path=Path('/data/dev_tools/affected_dependencies.json')),
                                                 'dependencies': JSON(path=Path('/data/dev_tools/dependencies.json')),
                                                 'diagram': Text(path=Path('/data/dev_tools/dependencies_diagram.mmd')),
                                                 'lock_file': TOML(path=Path('/uv.lock'))},
 'ordeq_dev_tools.pipelines.relevant_packages': {'affected_dependencies': JSON(path=Path('/data/dev_tools/affected_dependencies.json')),
                                                 'packages': JSON(path=Path('/data/dev_tools/changed_packages.json')),
                                                 'relevant_packages': JSON(path=Path('/data/dev_tools/relevant_packages.json'))},
 'ordeq_dev_tools.pipelines.viz_self': {'ordeq_dev_tools_diagram': Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))}}

```