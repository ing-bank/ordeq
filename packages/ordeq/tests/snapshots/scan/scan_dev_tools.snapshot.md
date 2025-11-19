## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._scan import scan

nodes, ios = scan(ordeq_dev_tools)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('ordeq_dev_tools.pipelines.docs_package_overview', 'packages'),
  View(name=ordeq_dev_tools.pipelines.shared:packages)),
 (('ordeq_dev_tools.pipelines.docs_package_overview', 'groups'),
  View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(id=ID1)])),
 (('ordeq_dev_tools.pipelines.docs_package_overview',
   'write_html_table_by_group'),
  Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(id=ID2)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))])),
 (('ordeq_dev_tools.pipelines.docs_update_just', 'just_output'),
  View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output)),
 (('ordeq_dev_tools.pipelines.docs_update_just', 'docs_just_section'),
  View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(id=ID3)])),
 (('ordeq_dev_tools.pipelines.docs_update_just',
   'update_docs_with_just_section'),
  Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID4)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))])),
 (('ordeq_dev_tools.pipelines.generate_draft_releases', 'packages'),
  View(name=ordeq_dev_tools.pipelines.shared:packages)),
 (('ordeq_dev_tools.pipelines.generate_draft_releases', 'draft_releases'),
  View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases)),
 (('ordeq_dev_tools.pipelines.generate_draft_releases', 'new_releases'),
  View(name=ordeq_dev_tools.pipelines.generate_draft_releases:new_releases, inputs=[IO(id=ID1)])),
 (('ordeq_dev_tools.pipelines.generate_draft_releases', 'create_releases'),
  View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[IO(id=ID5), IO(id=ID6)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'tags'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:tags, inputs=[Input(id=ID7)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_tag'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_tag, inputs=[IO(id=ID8)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_version'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_version, inputs=[IO(id=ID9)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'commits_since_tag'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag, inputs=[IO(id=ID9)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_hashes'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes, inputs=[IO(id=ID10)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_changed_files'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files, inputs=[IO(id=ID11)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_commits'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits, inputs=[IO(id=ID11), IO(id=ID12), Input(id=ID7)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_prs'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs, inputs=[IO(id=ID13)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'distinct_labels'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels, inputs=[IO(id=ID14)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_type'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_type, inputs=[IO(id=ID15)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_version'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_version, inputs=[IO(id=ID16), IO(id=ID17)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'get_new_tag'),
  Node(name=ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag, inputs=[Input(id=ID7), IO(id=ID18)], outputs=[IO(id=ID19)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'changes'),
  View(name=ordeq_dev_tools.pipelines.generate_release_notes:changes, inputs=[IO(id=ID13), IO(id=ID10), IO(id=ID14)])),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'create_release_notes'),
  Node(name=ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes, inputs=[IO(id=ID20)], outputs=[IO(id=ID21)])),
 (('ordeq_dev_tools.pipelines.list_changed_packages', 'changed_files'),
  View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files)),
 (('ordeq_dev_tools.pipelines.list_changed_packages',
   'extract_changed_packages'),
  Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(id=ID22)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))])),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'parse_dependencies'),
  Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))])),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'generate_mermaid_diagram'),
  Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))])),
 (('ordeq_dev_tools.pipelines.list_dependencies',
   'compute_affected_dependencies'),
  Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))])),
 (('ordeq_dev_tools.pipelines.relevant_packages', 'extract_relevant_packages'),
  Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))])),
 (('ordeq_dev_tools.pipelines.shared', 'packages'),
  View(name=ordeq_dev_tools.pipelines.shared:packages)),
 (('ordeq_dev_tools.pipelines.viz_self', 'visualize_ordeq_dev_tools'),
  Node(name=ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]))]
IOs:
[(('ordeq_dev_tools.pipelines.docs_package_overview', 'package_overview'),
  TextLinesStream(path=Path('/docs/packages.md'))),
 (('ordeq_dev_tools.pipelines.docs_update_just', 'contribution_guide'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (('ordeq_dev_tools.pipelines.docs_update_just', 'docs_file'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (('ordeq_dev_tools.pipelines.docs_update_just', 'updated_docs_file'),
  Text(path=Path('/docs/CONTRIBUTING.md'))),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'package'),
  Input(id=ID7)),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'release_notes'),
  IO(id=ID21)),
 (('ordeq_dev_tools.pipelines.generate_release_notes', 'new_tag'),
  IO(id=ID19)),
 (('ordeq_dev_tools.pipelines.list_changed_packages', 'changed_packages'),
  JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'lock_file'),
  TOML(path=Path('/uv.lock'))),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'dependencies'),
  JSON(path=Path('/data/dev_tools/dependencies.json'))),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'diagram'),
  Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))),
 (('ordeq_dev_tools.pipelines.list_dependencies', 'affected_dependencies'),
  JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 (('ordeq_dev_tools.pipelines.relevant_packages', 'affected_dependencies'),
  JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 (('ordeq_dev_tools.pipelines.relevant_packages', 'packages'),
  JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 (('ordeq_dev_tools.pipelines.relevant_packages', 'relevant_packages'),
  JSON(path=Path('/data/dev_tools/relevant_packages.json'))),
 (('ordeq_dev_tools.pipelines.viz_self', 'ordeq_dev_tools_diagram'),
  Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd')))]

```