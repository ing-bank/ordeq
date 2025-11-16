## Resource

```python
import ordeq_dev_tools
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_mermaid import pipeline_to_mermaid

nodes, ios = _resolve_runnables_to_nodes_and_ios(ordeq_dev_tools)
diagram = pipeline_to_mermaid(nodes=nodes, ios=ios, subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Input"}
		L02@{shape: rect, label: "JSON"}
		L03@{shape: rect, label: "TOML"}
		L04@{shape: rect, label: "Text"}
		L05@{shape: rect, label: "TextLinesStream"}
	end

	ordeq_dev_tools.pipelines.shared:packages --> ordeq_dev_tools.pipelines.docs_package_overview:groups
	ordeq_dev_tools.pipelines.docs_package_overview:groups --> ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
	ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> IO0
	ordeq_dev_tools.pipelines.docs_update_just:just_output --> ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
	IO1 --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> IO2
	ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.shared:packages --> ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
	ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> ordeq_dev_tools.pipelines.generate_release_notes:bump_type
	ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
	ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
	ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
	ordeq_dev_tools.pipelines.generate_release_notes:changes --> ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
	ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> IO3
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
	IO4 --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> IO5
	ordeq_dev_tools.pipelines.generate_release_notes:tags --> ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
	ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> ordeq_dev_tools.pipelines.generate_release_notes:latest_version
	ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	IO4 --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
	IO4 --> ordeq_dev_tools.pipelines.generate_release_notes:tags
	ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
	ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> IO6
	IO7 --> ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> IO8
	IO7 --> ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
	ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> IO9
	IO10 --> ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> IO7
	IO11 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	IO12 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> IO13
	ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> IO14

	subgraph s0["ordeq_dev_tools.pipelines.docs_package_overview"]
		direction TB
		ordeq_dev_tools.pipelines.docs_package_overview:groups@{shape: subroutine, label: "groups"}
		ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group@{shape: rounded, label: "write_html_table_by_group"}
	end
	subgraph s1["ordeq_dev_tools.pipelines.docs_update_just"]
		direction TB
		ordeq_dev_tools.pipelines.docs_update_just:docs_just_section@{shape: subroutine, label: "docs_just_section"}
		ordeq_dev_tools.pipelines.docs_update_just:just_output@{shape: subroutine, label: "just_output"}
		ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section@{shape: rounded, label: "update_docs_with_just_section"}
	end
	subgraph s2["ordeq_dev_tools.pipelines.generate_draft_releases"]
		direction TB
		ordeq_dev_tools.pipelines.generate_draft_releases:create_releases@{shape: subroutine, label: "create_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases@{shape: subroutine, label: "draft_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:new_releases@{shape: subroutine, label: "new_releases"}
	end
	subgraph s3["ordeq_dev_tools.pipelines.generate_release_notes"]
		direction TB
		ordeq_dev_tools.pipelines.generate_release_notes:bump_type@{shape: subroutine, label: "bump_type"}
		ordeq_dev_tools.pipelines.generate_release_notes:bump_version@{shape: subroutine, label: "bump_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:changes@{shape: subroutine, label: "changes"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files@{shape: subroutine, label: "commit_changed_files"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes@{shape: subroutine, label: "commit_hashes"}
		ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag@{shape: subroutine, label: "commits_since_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes@{shape: rounded, label: "create_release_notes"}
		ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels@{shape: subroutine, label: "distinct_labels"}
		ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag@{shape: rounded, label: "get_new_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_tag@{shape: subroutine, label: "latest_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_version@{shape: subroutine, label: "latest_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits@{shape: subroutine, label: "relevant_commits"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs@{shape: subroutine, label: "relevant_prs"}
		ordeq_dev_tools.pipelines.generate_release_notes:tags@{shape: subroutine, label: "tags"}
	end
	subgraph s4["ordeq_dev_tools.pipelines.list_changed_packages"]
		direction TB
		ordeq_dev_tools.pipelines.list_changed_packages:changed_files@{shape: subroutine, label: "changed_files"}
		ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages@{shape: rounded, label: "extract_changed_packages"}
	end
	subgraph s5["ordeq_dev_tools.pipelines.list_dependencies"]
		direction TB
		ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies@{shape: rounded, label: "compute_affected_dependencies"}
		ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram@{shape: rounded, label: "generate_mermaid_diagram"}
		ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies@{shape: rounded, label: "parse_dependencies"}
		IO7@{shape: rect, label: "dependencies"}
	end
	subgraph s6["ordeq_dev_tools.pipelines.relevant_packages"]
		direction TB
		ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages@{shape: rounded, label: "extract_relevant_packages"}
	end
	subgraph s7["ordeq_dev_tools.pipelines.shared"]
		direction TB
		ordeq_dev_tools.pipelines.shared:packages@{shape: subroutine, label: "packages"}
	end
	subgraph s8["ordeq_dev_tools.pipelines.viz_self"]
		direction TB
		ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools@{shape: rounded, label: "visualize_ordeq_dev_tools"}
	end
	IO0@{shape: rect, label: "package_overview"}
	IO1@{shape: rect, label: "docs_file"}
	IO10@{shape: rect, label: "lock_file"}
	IO11@{shape: rect, label: "packages"}
	IO12@{shape: rect, label: "affected_dependencies"}
	IO13@{shape: rect, label: "relevant_packages"}
	IO14@{shape: rect, label: "ordeq_dev_tools_diagram"}
	IO2@{shape: rect, label: "updated_docs_file"}
	IO3@{shape: rect, label: "release_notes"}
	IO4@{shape: rect, label: "package"}
	IO5@{shape: rect, label: "new_tag"}
	IO6@{shape: rect, label: "changed_packages"}
	IO8@{shape: rect, label: "affected_dependencies"}
	IO9@{shape: rect, label: "diagram"}

	class L0,ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group,ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section,ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes,ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag,ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages,ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies,ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram,ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies,ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages,ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools node
	class L2,ordeq_dev_tools.pipelines.docs_package_overview:groups,ordeq_dev_tools.pipelines.docs_update_just:docs_just_section,ordeq_dev_tools.pipelines.docs_update_just:just_output,ordeq_dev_tools.pipelines.generate_draft_releases:create_releases,ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases,ordeq_dev_tools.pipelines.generate_draft_releases:new_releases,ordeq_dev_tools.pipelines.generate_release_notes:bump_type,ordeq_dev_tools.pipelines.generate_release_notes:bump_version,ordeq_dev_tools.pipelines.generate_release_notes:changes,ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files,ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes,ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag,ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels,ordeq_dev_tools.pipelines.generate_release_notes:latest_tag,ordeq_dev_tools.pipelines.generate_release_notes:latest_version,ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits,ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs,ordeq_dev_tools.pipelines.generate_release_notes:tags,ordeq_dev_tools.pipelines.list_changed_packages:changed_files,ordeq_dev_tools.pipelines.shared:packages view
	class L00,IO3,IO5 io0
	class L01,IO4 io1
	class L02,IO7,IO11,IO12,IO13,IO6,IO8 io2
	class L03,IO10 io3
	class L04,IO1,IO14,IO2,IO9 io4
	class L05,IO0 io5
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3
	classDef io4 fill:#a6d854
	classDef io5 fill:#ffd92f


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
WARNING	ordeq_viz.to_mermaid	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```