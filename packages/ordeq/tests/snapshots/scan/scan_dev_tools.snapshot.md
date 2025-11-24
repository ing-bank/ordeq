## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(ordeq_dev_tools))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
Nodes:
[(FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='packages'),
  View(func=ordeq_dev_tools.pipelines.shared:packages)),
 (FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='packages'),
  View(func=ordeq_dev_tools.pipelines.shared:packages)),
 (FQN(module='ordeq_dev_tools.pipelines.shared', name='packages'),
  View(func=ordeq_dev_tools.pipelines.shared:packages)),
 (FQN(module='ordeq_dev_tools.pipelines.validate_pyproject', name='packages'),
  View(func=ordeq_dev_tools.pipelines.shared:packages)),
 (FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='groups'),
  View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID1)])),
 (FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='write_html_table_by_group'),
  Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID2)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))])),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='just_output'),
  View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output)),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='docs_just_section'),
  View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID3)])),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='update_docs_with_just_section'),
  Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID4)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='draft_releases'),
  View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases)),
 (FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='new_releases'),
  View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID1)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='create_releases'),
  View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID5), IO(id=ID6)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='tags'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[Input(id=ID7)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='latest_tag'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID8)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='latest_version'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID9)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commits_since_tag'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID9)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commit_hashes'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID10)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commit_changed_files'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID11)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='relevant_commits'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID11), IO(id=ID12), Input(id=ID7)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='relevant_prs'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID13)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='distinct_labels'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID14)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='bump_type'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID15)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='bump_version'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID16), IO(id=ID17)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='get_new_tag'),
  Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[Input(id=ID7), IO(id=ID18)], outputs=[IO(id=ID19)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='changes'),
  View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID13), IO(id=ID10), IO(id=ID14)])),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='create_release_notes'),
  Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID20)], outputs=[IO(id=ID21)])),
 (FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='changed_files'),
  View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files)),
 (FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='extract_changed_packages'),
  Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID22)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))])),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='parse_dependencies'),
  Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))])),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='generate_mermaid_diagram'),
  Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))])),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='compute_affected_dependencies'),
  Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))])),
 (FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='extract_relevant_packages'),
  Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))])),
 (FQN(module='ordeq_dev_tools.pipelines.validate_pyproject', name='groups'),
  View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID1)])),
 (FQN(module='ordeq_dev_tools.pipelines.viz_self', name='visualize_ordeq_dev_tools'),
  Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]))]
IOs:
[(FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='package_overview'),
  TextLinesStream(path=Path('/docs/packages.md'))),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='contribution_guide'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='docs_file'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='updated_docs_file'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='package'),
  Input(id=ID7)),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='release_notes'),
  IO(id=ID21)),
 (FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='new_tag'),
  IO(id=ID19)),
 (FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='changed_packages'),
  JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='lock_file'),
  TOML(path=Path('/uv.lock'))),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='dependencies'),
  JSON(path=Path('/data/dev_tools/dependencies.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='diagram'),
  Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))),
 (FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='affected_dependencies'),
  JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='affected_dependencies'),
  JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='packages'),
  JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='relevant_packages'),
  JSON(path=Path('/data/dev_tools/relevant_packages.json'))),
 (FQN(module='ordeq_dev_tools.pipelines.viz_self', name='ordeq_dev_tools_diagram'),
  Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd')))]

```