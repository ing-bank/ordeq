## Resource

```python
# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
base_graph = NodeIOGraph.from_nodes(nodes)
print(base_graph)
node_graph = NodeGraph.from_graph(base_graph)
pprint(node_graph.topological_ordering)

```

## Output

```text
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-1
io-1 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-2
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-3
io-3 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> io-4
io-4 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-5
Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> io-6
io-6 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-7
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-8
io-8 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> io-9
io-9 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-9 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-10
io-10 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
io-10 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-11
io-11 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> io-12
io-12 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-12 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> io-13
io-13 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> io-14
io-14 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> io-15
io-15 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> io-16
io-16 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-17
io-17 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-18
io-18 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-19
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-20
io-20 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-20 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-21
View:ordeq_dev_tools.pipelines.shared:packages --> io-22
io-22 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-22 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-23
(View(name=ordeq_dev_tools.pipelines.shared:packages),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:package_tags, inputs=[IO(idx=ID1)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags, inputs=[IO(idx=ID2)], outputs=[IO(idx=ID3)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits, inputs=[IO(idx=ID3)], outputs=[IO(idx=ID4), IO(idx=ID5)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files, inputs=[IO(idx=ID4)], outputs=[IO(idx=ID6)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID4), IO(idx=ID6)], outputs=[IO(idx=ID7)]),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs, inputs=[IO(idx=ID7)], outputs=[IO(idx=ID8)]),
 View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(idx=ID9)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID3), IO(idx=ID7), IO(idx=ID8), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]),
 View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(idx=ID10)]),
 View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(idx=ID1)]),
 Node(name=ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]),
 Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[JSON(path=Path('/data/dev_tools/change_report.json')), IO(idx=ID11)]),
 Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(idx=ID12)], outputs=[Text(path=Path('/docs/CONTRIBUTING_NEW.md'))]),
 Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(idx=ID13)], outputs=[Text(path=Path('/docs/packages.md'))]))

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