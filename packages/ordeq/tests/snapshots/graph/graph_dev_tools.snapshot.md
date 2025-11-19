## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
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
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-19
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-20
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-21
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
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
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
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.shared:packages'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_package_overview:groups'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:just_output'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:tags'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:latest_tag'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:latest_version'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:bump_type'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:bump_version'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_release_notes:changes'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:new_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.generate_draft_releases:create_releases'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```