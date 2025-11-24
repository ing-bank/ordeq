## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
fq_nodes_and_views = _collect_views(*fqn_nodes)
nodes_and_views = [node for _, node in fq_nodes_and_views]
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
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> io-7
io-7 --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
io-7 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> io-8
io-8 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> io-10
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> io-11
View:View(func=ordeq_dev_tools.pipelines.shared:packages) --> io-12
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output) --> io-13
io-9 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
io-10 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-11 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-12 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-12 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
io-12 --> View:ordeq_dev_tools.pipelines.validate_pyproject:groups
io-13 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-14
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> io-17
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> io-18
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases) --> io-19
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-20
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-21
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-23
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files) --> io-24
io-14 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-14 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
io-15 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-16 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-17 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
io-18 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
io-19 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-20 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-21 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-22 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-23 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
io-24 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-25
View:ordeq_dev_tools.pipelines.validate_pyproject:groups --> io-26
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-27
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> io-28
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> io-29
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-30
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-31
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-32
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-33
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-34
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-35
NodeGraph
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> View:ordeq_dev_tools.pipelines.generate_release_notes:tags
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:View(func=ordeq_dev_tools.pipelines.shared:packages) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages)
View:View(func=ordeq_dev_tools.pipelines.shared:packages) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages)
View:View(func=ordeq_dev_tools.pipelines.shared:packages) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages)
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output) --> View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output)
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files) --> Node:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files)
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases) --> View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases)
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> Node:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> Node:ordeq_dev_tools.pipelines.generate_release_notes:changes
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
View:ordeq_dev_tools.pipelines.validate_pyproject:groups
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Topological ordering
(View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[Input(id=ID1)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID2)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID3)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID4)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID5)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID5), IO(id=ID6), Input(id=ID1)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID7)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID8)]),
 View(func=ordeq_dev_tools.pipelines.shared:packages),
 View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID3)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID9)]),
 View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID10)]),
 View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID11)]),
 View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID10)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID12), IO(id=ID13)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID7), IO(id=ID4), IO(id=ID8)]),
 Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID14)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]),
 Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID15)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]),
 Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID16)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID17), IO(id=ID18)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[Input(id=ID1), IO(id=ID19)], outputs=[IO(id=ID20)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID21)], outputs=[IO(id=ID22)]),
 Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID10)]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]))

```

## Logging

```text
WARNING	ordeq.preview	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.

```