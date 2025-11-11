## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
base_graph = NodeIOGraph.from_nodes({node for _, _, node in nodes})
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
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-1
io-1 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-2
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-3
io-3 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> io-4
io-4 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-5
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-6
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> io-7
io-7 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-8
io-8 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> io-9
io-9 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> io-10
io-10 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> io-11
io-11 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> io-12
io-12 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> io-13
io-13 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
io-13 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> io-14
io-14 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
io-14 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> io-15
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> io-16
io-16 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> io-17
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> io-18
io-18 --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
io-18 --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> io-19
io-19 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> io-20
io-20 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
io-20 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> io-21
io-21 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
io-21 --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> io-22
io-22 --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> io-23
io-23 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-24
io-24 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-25
io-25 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-26
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-27
io-27 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-27 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-28
View:ordeq_dev_tools.pipelines.shared:packages --> io-29
io-29 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-29 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-30
io-31 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-32 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
io-32 --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
io-32 --> View:ordeq_dev_tools.pipelines.generate_release_notes:tags
io-33 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
NodeGraph
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.docs_update_just:just_output --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.shared:packages --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
Topological ordering
['ordeq_dev_tools.pipelines.generate_release_notes:tags',
 'ordeq_dev_tools.pipelines.generate_release_notes:latest_tag',
 'ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag',
 'ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes',
 'ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files',
 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits',
 'ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs',
 'ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels',
 'ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:changed_files',
 'ordeq_dev_tools.pipelines.generate_release_notes:latest_version',
 'ordeq_dev_tools.pipelines.generate_release_notes:bump_type',
 'ordeq_dev_tools.pipelines.shared:packages',
 'ordeq_dev_tools.pipelines.docs_update_just:just_output',
 'ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies',
 'ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages',
 'ordeq_dev_tools.pipelines.generate_release_notes:changes',
 'ordeq_dev_tools.pipelines.generate_release_notes:bump_version',
 'ordeq_dev_tools.pipelines.generate_draft_releases:new_releases',
 'ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases',
 'ordeq_dev_tools.pipelines.docs_update_just:docs_just_section',
 'ordeq_dev_tools.pipelines.docs_package_overview:groups',
 'ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools',
 'ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram',
 'ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages',
 'ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes',
 'ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag',
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