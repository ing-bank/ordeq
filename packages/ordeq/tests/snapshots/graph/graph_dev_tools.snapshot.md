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
<ordeq._graph.NodeIOGraph object at HASH1>
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