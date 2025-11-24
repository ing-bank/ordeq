## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(ordeq_dev_tools)
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
[View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID1)]),
 View(func=ordeq_dev_tools.pipelines.shared:packages),
 Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID2)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]),
 View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID3)]),
 View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID4)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID5), IO(id=ID6)]),
 View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID1)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID7)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID8), IO(id=ID9)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID10), IO(id=ID11), IO(id=ID12)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID13)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID11)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID14)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID15)], outputs=[IO(id=ID16)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID12)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[Input(id=ID17), IO(id=ID18)], outputs=[IO(id=ID19)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID20)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID14)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID13), IO(id=ID21), Input(id=ID17)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID10)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[Input(id=ID17)]),
 View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID22)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID1)]),
 Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))])]
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