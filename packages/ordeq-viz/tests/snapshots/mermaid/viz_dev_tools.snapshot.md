## Resource

```python
import ordeq_dev_tools
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(ordeq_dev_tools)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "JSON"}
		L02@{shape: rect, label: "TOML"}
		L03@{shape: rect, label: "Text"}
		L04@{shape: rect, label: "TextLinesStream"}
	end

	IO0 --> ordeq_dev_tools.pipelines.docs_package_overview:groups
	ordeq_dev_tools.pipelines.docs_package_overview:groups --> IO1
	IO1 --> ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
	ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> IO2
	IO3 --> ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
	ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> IO4
	ordeq_dev_tools.pipelines.docs_update_just:just_output --> IO3
	IO5 --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	IO4 --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> IO6
	IO7 --> ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
	IO8 --> ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
	IO9 --> ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
	IO10 --> ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes
	ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes --> IO11
	IO11 --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	IO12 --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> IO13
	ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> IO12
	IO14 --> ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
	IO15 --> ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node
	ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node --> IO8
	IO7 --> ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits
	ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> IO14
	ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits --> IO10
	IO16 --> ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags
	ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags --> IO7
	IO14 --> ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files
	ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files --> IO15
	IO8 --> ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs
	ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs --> IO9
	IO0 --> ordeq_dev_tools.pipelines.generate_draft_releases:package_tags
	ordeq_dev_tools.pipelines.generate_draft_releases:package_tags --> IO16
	ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> IO17
	IO17 --> ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
	ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> IO18
	IO19 --> ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> IO20
	IO19 --> ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
	ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> IO21
	IO22 --> ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> IO19
	IO18 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	IO20 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> IO23
	ordeq_dev_tools.pipelines.shared:packages --> IO0
	ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> IO24

	subgraph s0["ordeq_dev_tools.pipelines.docs_package_overview"]
		direction TB
		ordeq_dev_tools.pipelines.docs_package_overview:groups@{shape: rounded, label: "groups"}
		ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group@{shape: rounded, label: "write_html_table_by_group"}
		IO1@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s1["ordeq_dev_tools.pipelines.docs_update_just"]
		direction TB
		ordeq_dev_tools.pipelines.docs_update_just:docs_just_section@{shape: rounded, label: "docs_just_section"}
		ordeq_dev_tools.pipelines.docs_update_just:just_output@{shape: rounded, label: "just_output"}
		ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section@{shape: rounded, label: "update_docs_with_just_section"}
		IO3@{shape: rect, label: "&lt;anonymous&gt;"}
		IO4@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s2["ordeq_dev_tools.pipelines.generate_draft_releases"]
		direction TB
		ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes@{shape: rounded, label: "compute_package_changes"}
		ordeq_dev_tools.pipelines.generate_draft_releases:create_releases@{shape: rounded, label: "create_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases@{shape: rounded, label: "draft_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node@{shape: rounded, label: "filter_commits_by_package_node"}
		ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits@{shape: rounded, label: "get_all_commits"}
		ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags@{shape: rounded, label: "get_all_latest_tags"}
		ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files@{shape: rounded, label: "get_commit_changed_files"}
		ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs@{shape: rounded, label: "get_relevant_prs"}
		ordeq_dev_tools.pipelines.generate_draft_releases:package_tags@{shape: rounded, label: "package_tags"}
		IO10@{shape: rect, label: "commit_messages"}
		IO11@{shape: rect, label: "changes"}
		IO12@{shape: rect, label: "&lt;anonymous&gt;"}
		IO14@{shape: rect, label: "package_commits"}
		IO15@{shape: rect, label: "commit_changes"}
		IO16@{shape: rect, label: "&lt;anonymous&gt;"}
		IO7@{shape: rect, label: "package_latest_tags"}
		IO8@{shape: rect, label: "package_relevant_commits"}
		IO9@{shape: rect, label: "package_relevant_prs"}
	end
	subgraph s3["ordeq_dev_tools.pipelines.list_changed_packages"]
		direction TB
		ordeq_dev_tools.pipelines.list_changed_packages:changed_files@{shape: rounded, label: "changed_files"}
		ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages@{shape: rounded, label: "extract_changed_packages"}
		IO17@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s4["ordeq_dev_tools.pipelines.list_dependencies"]
		direction TB
		ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies@{shape: rounded, label: "compute_affected_dependencies"}
		ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram@{shape: rounded, label: "generate_mermaid_diagram"}
		ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies@{shape: rounded, label: "parse_dependencies"}
		IO19@{shape: rect, label: "dependencies"}
	end
	subgraph s5["ordeq_dev_tools.pipelines.relevant_packages"]
		direction TB
		ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages@{shape: rounded, label: "extract_relevant_packages"}
	end
	subgraph s6["ordeq_dev_tools.pipelines.shared"]
		direction TB
		ordeq_dev_tools.pipelines.shared:packages@{shape: rounded, label: "packages"}
	end
	subgraph s7["ordeq_dev_tools.pipelines.viz_self"]
		direction TB
		ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools@{shape: rounded, label: "visualize_ordeq_dev_tools"}
	end
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO13@{shape: rect, label: "&lt;anonymous&gt;"}
	IO18@{shape: rect, label: "packages"}
	IO2@{shape: rect, label: "package_overview"}
	IO20@{shape: rect, label: "affected_dependencies"}
	IO21@{shape: rect, label: "diagram"}
	IO22@{shape: rect, label: "lock_file"}
	IO23@{shape: rect, label: "relevant_packages"}
	IO24@{shape: rect, label: "ordeq_dev_tools_diagram"}
	IO5@{shape: rect, label: "docs_file"}
	IO6@{shape: rect, label: "updated_docs_file"}

	class L0,ordeq_dev_tools.pipelines.docs_package_overview:groups,ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group,ordeq_dev_tools.pipelines.docs_update_just:docs_just_section,ordeq_dev_tools.pipelines.docs_update_just:just_output,ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section,ordeq_dev_tools.pipelines.generate_draft_releases:compute_package_changes,ordeq_dev_tools.pipelines.generate_draft_releases:create_releases,ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases,ordeq_dev_tools.pipelines.generate_draft_releases:filter_commits_by_package_node,ordeq_dev_tools.pipelines.generate_draft_releases:get_all_commits,ordeq_dev_tools.pipelines.generate_draft_releases:get_all_latest_tags,ordeq_dev_tools.pipelines.generate_draft_releases:get_commit_changed_files,ordeq_dev_tools.pipelines.generate_draft_releases:get_relevant_prs,ordeq_dev_tools.pipelines.generate_draft_releases:package_tags,ordeq_dev_tools.pipelines.list_changed_packages:changed_files,ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages,ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies,ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram,ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies,ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages,ordeq_dev_tools.pipelines.shared:packages,ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools node
	class L00,IO1,IO3,IO4,IO10,IO12,IO14,IO15,IO16,IO7,IO8,IO9,IO17,IO0,IO13 io0
	class L01,IO11,IO19,IO18,IO20,IO23 io1
	class L02,IO22 io2
	class L03,IO21,IO24,IO5,IO6 io3
	class L04,IO2 io4
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854


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