## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_graph(base_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
io-1 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
io-2 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
io-3 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
io-4 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-5 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-6 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
io-7 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
io-7 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-8 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
io-8 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
io-9 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
io-10 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
io-10 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-11 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
io-11 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-12 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-13 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
io-14 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-15 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-16 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-16 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
io-17 --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
io-18 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-19 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-7
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> io-3
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> io-2
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-4
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-15
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-20
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-21
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-5
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> io-11
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-22
Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> io-18
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> io-12
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-23
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-6
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-8
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> io-13
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> io-9
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-24
View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> io-17
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-19
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> io-10
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-25
View:ordeq_dev_tools.pipelines.shared:packages --> io-16
NodeGraph
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
Node:ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> Node:ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
Topological ordering
['ordeq_dev_tools.pipelines.shared:packages',
 'ordeq_dev_tools.pipelines.generate_draft_releases:package_tags',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files',
 'ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node',
 'ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs',
 'ordeq_dev_tools.pipelines.docs_update_just:just_output',
 'ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files',
 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases',
 'ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes',
 'ordeq_dev_tools.pipelines.docs_package_overview:groups',
 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section',
 'ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages',
 'ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools',
 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases',
 'ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group',
 'ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section',
 'ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages',
 'ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram']

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