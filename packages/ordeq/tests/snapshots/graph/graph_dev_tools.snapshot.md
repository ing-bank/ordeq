## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph, _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
nodes = [node for _, _, node in fqn_nodes]
nodes_and_views = _collect_views(*nodes)
base_graph = NodeIOGraph.from_nodes(nodes_and_views)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes_and_views)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

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
View:ordeq_dev_tools.pipelines.shared:packages --> io-12
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> io-13
io-9 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
io-10 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-11 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-12 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-12 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
io-13 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-14
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> io-17
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> io-18
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-19
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-20
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-22
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-23
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> io-24
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
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-26
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> io-27
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> io-28
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-29
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-30
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-31
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-32
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-33
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-34
NodeGraph
NodeGraph(edges={View(name=ordeq_dev_tools.pipelines.generate_release_notes:tags, inputs=[Input(id=ID1)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_tag, inputs=[IO(id=ID2)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_tag, inputs=[IO(id=ID2)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_version, inputs=[IO(id=ID3)]), View(name=ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag, inputs=[IO(id=ID3)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag, inputs=[IO(id=ID3)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes, inputs=[IO(id=ID4)]), View(name=ordeq_dev_tools.pipelines.generate_release_notes:changes, inputs=[IO(id=ID5), IO(id=ID4), IO(id=ID6)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes, inputs=[IO(id=ID4)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files, inputs=[IO(id=ID7)]), View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits, inputs=[IO(id=ID7), IO(id=ID8), Input(id=ID1)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files, inputs=[IO(id=ID7)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits, inputs=[IO(id=ID7), IO(id=ID8), Input(id=ID1)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits, inputs=[IO(id=ID7), IO(id=ID8), Input(id=ID1)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs, inputs=[IO(id=ID5)]), View(name=ordeq_dev_tools.pipelines.generate_release_notes:changes, inputs=[IO(id=ID5), IO(id=ID4), IO(id=ID6)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs, inputs=[IO(id=ID5)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels, inputs=[IO(id=ID6)]), View(name=ordeq_dev_tools.pipelines.generate_release_notes:changes, inputs=[IO(id=ID5), IO(id=ID4), IO(id=ID6)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels, inputs=[IO(id=ID6)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_type, inputs=[IO(id=ID9)])], Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]): [Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]), Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))])], View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files): [Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(id=ID10)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_type, inputs=[IO(id=ID9)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_version, inputs=[IO(id=ID11), IO(id=ID12)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:latest_version, inputs=[IO(id=ID3)]): [View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_version, inputs=[IO(id=ID11), IO(id=ID12)])], View(name=ordeq_dev_tools.pipelines.shared:packages): [View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(id=ID13)]), View(name=ordeq_dev_tools.pipelines.generate_draft_releases:new_releases, inputs=[IO(id=ID13)])], View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output): [View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(id=ID14)])], Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]): [Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))])], Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(id=ID10)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]): [Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:changes, inputs=[IO(id=ID5), IO(id=ID4), IO(id=ID6)]): [Node(name=ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes, inputs=[IO(id=ID15)], outputs=[IO(id=ID16)])], View(name=ordeq_dev_tools.pipelines.generate_release_notes:bump_version, inputs=[IO(id=ID11), IO(id=ID12)]): [Node(name=ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag, inputs=[Input(id=ID1), IO(id=ID17)], outputs=[IO(id=ID18)])], View(name=ordeq_dev_tools.pipelines.generate_draft_releases:new_releases, inputs=[IO(id=ID13)]): [View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[IO(id=ID19), IO(id=ID20)])], View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases): [View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[IO(id=ID19), IO(id=ID20)])], View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(id=ID14)]): [Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID21)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))])], View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(id=ID13)]): [Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(id=ID22)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))])], Node(name=ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]): [], Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]): [], Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]): [], Node(name=ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes, inputs=[IO(id=ID15)], outputs=[IO(id=ID16)]): [], Node(name=ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag, inputs=[Input(id=ID1), IO(id=ID17)], outputs=[IO(id=ID18)]): [], View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[IO(id=ID19), IO(id=ID20)]): [], Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(id=ID21)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]): [], Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(id=ID22)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]): []})
Topological ordering
['ordeq_dev_tools.pipelines.generate_release_notes:tags',
 'ordeq_dev_tools.pipelines.generate_release_notes:latest_tag',
 'ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag',
 'ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes',
 'ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files',
 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits',
 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs',
 'ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels',
 'ordeq_dev_tools.pipelines.shared:packages',
 'ordeq_dev_tools.pipelines.docs_update_just:just_output',
 'ordeq_dev_tools.pipelines.generate_release_notes:latest_version',
 'ordeq_dev_tools.pipelines.generate_release_notes:bump_type',
 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files',
 'ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies',
 'ordeq_dev_tools.pipelines.docs_package_overview:groups',
 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section',
 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases',
 'ordeq_dev_tools.pipelines.generate_draft_releases:new_releases',
 'ordeq_dev_tools.pipelines.generate_release_notes:bump_version',
 'ordeq_dev_tools.pipelines.generate_release_notes:changes',
 'ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages',
 'ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies',
 'ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools',
 'ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group',
 'ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section',
 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases',
 'ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag',
 'ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes',
 'ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages',
 'ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.shared:packages'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq_files.text_lines_stream	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_package_overview:groups'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:just_output'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:tags'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:latest_tag'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:latest_version'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:bump_type'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:bump_version'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:changes'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:new_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```