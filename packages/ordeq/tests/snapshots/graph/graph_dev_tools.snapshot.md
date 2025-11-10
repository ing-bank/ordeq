## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NamedNodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph")
print(named_node_io_graph)

node_graph = NodeGraph.from_graph(named_node_io_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NamedNodeIOGraph
io-0 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-0 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
io-1 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
io-3 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
io-5 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-4 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-7 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-7 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
io-8 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-8 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
io-9 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-10 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-11 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-12 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-14 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
io-14 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
io-15 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
io-16 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
io-17 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
io-19 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-19 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
io-22 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
io-18 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-20 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-1
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-2
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-4
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> io-3
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-6
Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> io-11
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-13
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-12
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> io-8
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-14
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-10
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> io-7
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> io-15
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> io-9
View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> io-16
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> io-17
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-18
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-20
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-21
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-19
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-23
View:ordeq_dev_tools.pipelines.shared:packages --> io-0
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-24
NodeGraph
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
Topological ordering
['ordeq_dev_tools.pipelines.shared:packages',
 'ordeq_dev_tools.pipelines.generate_draft_releases:package_tags',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files',
 'ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node',
 'ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs',
 'ordeq_dev_tools.pipelines.docs_update_just:just_output',
 'ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages',
 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases',
 'ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes',
 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section',
 'ordeq_dev_tools.pipelines.docs_package_overview:groups',
 'ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram',
 'ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages',
 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases',
 'ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section',
 'ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group']

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.shared:packages'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq_files.text_lines_stream	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_package_overview:groups'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:just_output'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:package_tags'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```