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
{'ordeq_dev_tools.pipelines.docs_package_overview': {'package_overview': Text(path=Path('/docs/packages.md'))},
 'ordeq_dev_tools.pipelines.docs_update_just': {'docs_file': Text(path=Path('/docs/CONTRIBUTING.md')),
                                                'updated_docs_file': Text(path=Path('/docs/CONTRIBUTING_NEW.md'))},
 'ordeq_dev_tools.pipelines.generate_draft_releases': {'changes': JSON(path=Path('/data/dev_tools/change_report.json')),
                                                       'commit_changes': IO(idx=ID1),
                                                       'commit_messages': IO(idx=ID2),
                                                       'package_commits': IO(idx=ID3),
                                                       'package_latest_tags': IO(idx=ID4),
                                                       'package_relevant_commits': IO(idx=ID5),
                                                       'package_relevant_prs': IO(idx=ID6),
                                                       'packages_dir': Literal(Path('/packages'))},
 'ordeq_dev_tools.pipelines.list_changed_packages': {'packages': JSON(path=Path('/data/dev_tools/changed_packages.json'))},
 'ordeq_dev_tools.pipelines.list_dependencies': {'affected_dependencies': JSON(path=Path('/data/dev_tools/affected_dependencies.json')),
                                                 'dependencies': JSON(path=Path('/data/dev_tools/dependencies.json')),
                                                 'diagram': Text(path=Path('/data/dev_tools/dependencies_diagram.mmd')),
                                                 'lock_file': TOML(path=Path('/uv.lock'))},
 'ordeq_dev_tools.pipelines.relevant_packages': {'affected_dependencies': JSON(path=Path('/data/dev_tools/affected_dependencies.json')),
                                                 'packages': JSON(path=Path('/data/dev_tools/changed_packages.json')),
                                                 'relevant_packages': JSON(path=Path('/data/dev_tools/relevant_packages.json'))},
 'ordeq_dev_tools.pipelines.viz_self': {'ordeq_dev_tools_diagram': Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))}}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.shared:packages'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_package_overview:groups'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:just_output'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:package_tags'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```