## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NamedNodeIOGraph, NodeGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
named_node_io_graph = NamedNodeIOGraph.from_nodes(nodes)
print("NamedNodeIOGraph:")
pprint(named_node_io_graph)

node_graph = NodeGraph.from_graph(named_node_io_graph)
print("NodeGraph:")
pprint(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NamedNodeIOGraph:
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
NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>,
                            {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): None,
                                                                                                                                                                                                                               Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits, inputs=[IO(idx=ID2)], outputs=[IO(idx=ID6), IO(idx=ID5)]): None},
                             Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs, inputs=[IO(idx=ID3)], outputs=[IO(idx=ID4)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): None},
                             Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]): {Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]): None},
                             Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID3)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs, inputs=[IO(idx=ID3)], outputs=[IO(idx=ID4)]): None,
                                                                                                                                                                                                                                                                                        Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): None},
                             Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]): {Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]): None,
                                                                                                                                                                                                                                                                                   Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]): None},
                             Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): {View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[JSON(path=Path('/data/dev_tools/change_report.json')), IO(idx=ID8)]): None},
                             Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits, inputs=[IO(idx=ID2)], outputs=[IO(idx=ID6), IO(idx=ID5)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID3)]): None,
                                                                                                                                                                                                                                                                         Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): None,
                                                                                                                                                                                                                                                                         Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID7)]): None},
                             Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID7)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID3)]): None},
                             Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(idx=ID9)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]): {Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]): None},
                             View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(idx=ID10)]): {Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(idx=ID11)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]): None},
                             View(name=ordeq_dev_tools.pipelines.shared:packages): {View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(idx=ID10)]): None,
                                                                                    View(name=ordeq_dev_tools.pipelines.generate_draft_releases:package_tags, inputs=[IO(idx=ID10)]): None},
                             View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files): {Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(idx=ID9)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]): None},
                             View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output): {View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(idx=ID12)]): None},
                             View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(idx=ID12)]): {Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(idx=ID13)], outputs=[Text(path=Path('/docs/CONTRIBUTING_NEW.md'))]): None},
                             View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases): {View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[JSON(path=Path('/data/dev_tools/change_report.json')), IO(idx=ID8)]): None},
                             View(name=ordeq_dev_tools.pipelines.generate_draft_releases:package_tags, inputs=[IO(idx=ID10)]): {Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]): None}}),
          nodes={Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs, inputs=[IO(idx=ID3)], outputs=[IO(idx=ID4)]): None,
                 Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID3)]): None,
                 Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(idx=ID11)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(idx=ID13)], outputs=[Text(path=Path('/docs/CONTRIBUTING_NEW.md'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits, inputs=[IO(idx=ID2)], outputs=[IO(idx=ID6), IO(idx=ID5)]): None,
                 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID7)]): None,
                 Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(idx=ID9)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]): None,
                 View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(idx=ID10)]): None,
                 View(name=ordeq_dev_tools.pipelines.shared:packages): None,
                 View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files): None,
                 View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output): None,
                 View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(idx=ID12)]): None,
                 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[JSON(path=Path('/data/dev_tools/change_report.json')), IO(idx=ID8)]): None,
                 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases): None,
                 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:package_tags, inputs=[IO(idx=ID10)]): None})
Topological ordering
(View(name=ordeq_dev_tools.pipelines.shared:packages),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:package_tags, inputs=[IO(idx=ID10)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags, inputs=[IO(idx=ID1)], outputs=[IO(idx=ID2)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits, inputs=[IO(idx=ID2)], outputs=[IO(idx=ID6), IO(idx=ID5)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID7)]),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node, inputs=[IO(idx=ID6), IO(idx=ID7)], outputs=[IO(idx=ID3)]),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies, inputs=[TOML(path=Path('/uv.lock'))], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 View(name=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs, inputs=[IO(idx=ID3)], outputs=[IO(idx=ID4)]),
 View(name=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(name=ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages, inputs=[IO(idx=ID9)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 Node(name=ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes, inputs=[IO(idx=ID2), IO(idx=ID3), IO(idx=ID4), IO(idx=ID5)], outputs=[JSON(path=Path('/data/dev_tools/change_report.json'))]),
 View(name=ordeq_dev_tools.pipelines.docs_update_just:docs_just_section, inputs=[IO(idx=ID12)]),
 View(name=ordeq_dev_tools.pipelines.docs_package_overview:groups, inputs=[IO(idx=ID10)]),
 Node(name=ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram, inputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]),
 Node(name=ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages, inputs=[JSON(path=Path('/data/dev_tools/changed_packages.json')), JSON(path=Path('/data/dev_tools/affected_dependencies.json'))], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 View(name=ordeq_dev_tools.pipelines.generate_draft_releases:create_releases, inputs=[JSON(path=Path('/data/dev_tools/change_report.json')), IO(idx=ID8)]),
 Node(name=ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section, inputs=[Text(path=Path('/docs/CONTRIBUTING.md')), IO(idx=ID13)], outputs=[Text(path=Path('/docs/CONTRIBUTING_NEW.md'))]),
 Node(name=ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group, inputs=[IO(idx=ID11)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]))

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