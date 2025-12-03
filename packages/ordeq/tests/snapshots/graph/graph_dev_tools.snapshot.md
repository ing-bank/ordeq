## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
nodes_and_views = _collect_views(*fqn_nodes)
base_graph = NodeIOGraph.from_nodes(nodes_and_views)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes_and_views)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
io-0 --> View:ordeq_dev_tools.pipelines.generate_release_notes:tags
io-0 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
io-0 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> io-1
io-1 --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> io-2
io-2 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
io-2 --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> io-3
io-3 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
io-3 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> io-4
io-4 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
io-4 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> io-5
io-5 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> io-6
io-6 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
io-6 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> io-7
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> io-8
io-7 --> View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages
io-7 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
io-7 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-7 --> View:ordeq_dev_tools.pipelines.validate_pyproject:groups
io-8 --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
io-8 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages --> io-9
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> io-10
io-9 --> View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages
io-10 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...) --> io-11
View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages --> io-12
View:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...) --> io-13
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> io-14
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> io-15
io-11 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
io-12 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
io-13 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
io-14 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-15 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-16 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-17
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-18
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs --> io-20
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...) --> io-21
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-22
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> io-23
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> io-24
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...) --> io-25
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-26
io-17 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
io-18 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-19 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-20 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes
io-21 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-22 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-23 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
io-24 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
io-25 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
io-26 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-26 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
io-27 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-28 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-48
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-49
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes --> io-50
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-51
Node:ordeq_dev_tools.pipelines.generate_gallery:generate_gallery --> io-52
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> io-53
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> io-54
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-55
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-56
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-57
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-58
View:ordeq_dev_tools.pipelines.validate_pyproject:groups --> io-59
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-60
NodeGraph
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:tags
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> Stub:View(func=ordeq_dev_tools.pipelines.shared:packages, ...)
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages --> Stub:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages --> Stub:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages
View:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...) --> Stub:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...)
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...) --> Stub:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...)
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Stub:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...) --> Stub:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...)
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> Stub:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...) --> Stub:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...)
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs --> Stub:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Stub:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Stub:ordeq_dev_tools.pipelines.docs_package_overview:groups
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> Stub:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
View:ordeq_dev_tools.pipelines.validate_pyproject:groups --> Stub:ordeq_dev_tools.pipelines.validate_pyproject:groups
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> Stub:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Stub:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> Stub:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Stub:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> Stub:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
Node:ordeq_dev_tools.pipelines.generate_gallery:generate_gallery --> Stub:ordeq_dev_tools.pipelines.generate_gallery:generate_gallery
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> Stub:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes --> Stub:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> Stub:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> Stub:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Topological ordering
(Stub(value=Input(id=ID1)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[Input(id=ID1)]),
 Stub(value=IO(id=ID2)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID2)]),
 Stub(value=IO(id=ID3)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID3)]),
 Stub(value=IO(id=ID4)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID4)]),
 Stub(value=IO(id=ID5)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID5)]),
 Stub(value=IO(id=ID6)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID5), IO(id=ID6), Input(id=ID1)]),
 Stub(value=IO(id=ID7)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID7)]),
 View(func=ordeq_dev_tools.pipelines.shared:packages),
 Stub(value=IO(id=ID8)),
 Stub(value=IO(id=ID9)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID8)]),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=filter_packages, inputs=[IO(id=ID9)]),
 Stub(value=IO(id=ID10)),
 Stub(value=IO(id=ID11)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID10)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID3)]),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=check_ios_packages, inputs=[IO(id=ID11)]),
 View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs),
 View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 Stub(value=TOML(path=Path('/uv.lock'))),
 Stub(value=IO(id=ID12)),
 Stub(value=IO(id=ID13)),
 Stub(value=IO(id=ID14)),
 Stub(value=IO(id=ID15)),
 Stub(value=IO(id=ID16)),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID7), IO(id=ID4), IO(id=ID8)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID13), IO(id=ID12)]),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID9)]),
 View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=generate_package_docs, inputs=[IO(id=ID15), IO(id=ID14)]),
 View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID16)]),
 View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID9)]),
 Stub(value=JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 Stub(value=JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 Stub(value=JSON(path=Path('/data/dev_tools/dependencies.json'))),
 Stub(value=IO(id=ID17)),
 Stub(value=IO(id=ID18)),
 Stub(value=IO(id=ID19)),
 Stub(value=IO(id=ID20)),
 Stub(value=IO(id=ID21)),
 Stub(value=IO(id=ID22)),
 Stub(value=IO(id=ID23)),
 Stub(value=existing),
 Stub(value=IO(id=ID24)),
 Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]),
 View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID9)]),
 Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]),
 Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID17)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID18)], outputs=[IO(id=ID25)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[Input(id=ID1), IO(id=ID19)], outputs=[IO(id=ID26)]),
 Node(module=ordeq_dev_tools.pipelines.generate_gallery, name=generate_gallery, outputs=[Text(path=Path('/docs/guides/gallery.md'))]),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID20), IO(id=ID21)]),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=generate_api_readmes, inputs=[IO(id=ID22)]),
 Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID23)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]),
 Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID24)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]),
 Stub(value=Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))),
 Stub(value=IO(id=ID27)),
 Stub(value=IO(id=ID28)),
 Stub(value=IO(id=ID29)),
 Stub(value=JSON(path=Path('/data/dev_tools/relevant_packages.json'))),
 Stub(value=JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 Stub(value=IO(id=ID30)),
 Stub(value=Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))),
 Stub(value=IO(id=ID31)),
 Stub(value=JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 Stub(value=IO(id=ID25)),
 Stub(value=IO(id=ID26)),
 Stub(value=IO(id=ID32)),
 Stub(value=Text(path=Path('/docs/guides/gallery.md'))),
 Stub(value=IO(id=ID33)),
 Stub(value=IO(id=ID34)),
 Stub(value=IO(id=ID35)),
 Stub(value=new),
 Stub(value=TextLinesStream(path=Path('/docs/packages.md'))))

```

## Logging

```text
WARNING	ordeq.preview	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.

```