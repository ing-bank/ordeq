## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(ordeq_dev_tools)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID1)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]): [FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='write_html_table_by_group')],
 Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID2)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]): [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='update_docs_with_just_section')],
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[Input(id=ID3), IO(id=ID4)], outputs=[IO(id=ID5)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='get_new_tag')],
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID6)], outputs=[IO(id=ID7)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='create_release_notes')],
 Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID8)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]): [FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='extract_changed_packages')],
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]): [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='parse_dependencies')],
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]): [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='generate_mermaid_diagram')],
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]): [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='compute_affected_dependencies')],
 Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]): [FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='extract_relevant_packages')],
 Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]): [FQN(module='ordeq_dev_tools.pipelines.viz_self', name='visualize_ordeq_dev_tools')],
 View(func=ordeq_dev_tools.pipelines.shared:packages): [FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='packages'),
                                                        FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='packages'),
                                                        FQN(module='ordeq_dev_tools.pipelines.shared', name='packages'),
                                                        FQN(module='ordeq_dev_tools.pipelines.validate_pyproject', name='packages')],
 View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID9)]): [FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='groups')],
 View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output): [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='just_output')],
 View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID10)]): [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='docs_just_section')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[Input(id=ID3)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='tags')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID11)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='latest_tag')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID12)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='latest_version')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID12)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commits_since_tag')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID13)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commit_hashes')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID14)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='commit_changed_files')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID14), IO(id=ID15), Input(id=ID3)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='relevant_commits')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID16)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='relevant_prs')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID17)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='distinct_labels')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID18)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='bump_type')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID19), IO(id=ID20)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='bump_version')],
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID16), IO(id=ID13), IO(id=ID17)]): [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='changes')],
 View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases): [FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='draft_releases')],
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID9)]): [FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='new_releases')],
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID21), IO(id=ID22)]): [FQN(module='ordeq_dev_tools.pipelines.generate_draft_releases', name='create_releases')],
 View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files): [FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='changed_files')],
 View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID9)]): [FQN(module='ordeq_dev_tools.pipelines.validate_pyproject', name='groups')]}
IOs:
[[FQN(module='ordeq_dev_tools.pipelines.docs_package_overview', name='package_overview')],
 [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='contribution_guide')],
 [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='docs_file')],
 [FQN(module='ordeq_dev_tools.pipelines.docs_update_just', name='updated_docs_file')],
 [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='package')],
 [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='release_notes')],
 [FQN(module='ordeq_dev_tools.pipelines.generate_release_notes', name='new_tag')],
 [FQN(module='ordeq_dev_tools.pipelines.list_changed_packages', name='changed_packages')],
 [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='lock_file')],
 [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='dependencies')],
 [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='diagram')],
 [FQN(module='ordeq_dev_tools.pipelines.list_dependencies', name='affected_dependencies')],
 [FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='affected_dependencies')],
 [FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='packages')],
 [FQN(module='ordeq_dev_tools.pipelines.relevant_packages', name='relevant_packages')],
 [FQN(module='ordeq_dev_tools.pipelines.viz_self', name='ordeq_dev_tools_diagram')]]

```