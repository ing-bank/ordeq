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
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Input"}
		L02@{shape: rect, label: "JSON"}
		L03@{shape: rect, label: "TOML"}
		L04@{shape: rect, label: "Text"}
		L05@{shape: rect, label: "TextLinesStream"}
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
	IO7 --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	IO8 --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> IO9
	ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> IO8
	IO0 --> ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> IO7
	IO10 --> ordeq_dev_tools.pipelines.generate_release_notes:bump_type
	ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> IO11
	IO12 --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	IO11 --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> IO13
	IO14 --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	IO15 --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	IO16 --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:changes --> IO17
	IO18 --> ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
	ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> IO19
	IO15 --> ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
	ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> IO18
	IO20 --> ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
	ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> IO15
	IO17 --> ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
	ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> IO21
	IO16 --> ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
	ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> IO10
	IO22 --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	IO13 --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> IO23
	IO24 --> ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
	ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> IO20
	IO20 --> ordeq_dev_tools.pipelines.generate_release_notes:latest_version
	ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> IO12
	IO18 --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	IO19 --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	IO22 --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> IO14
	IO14 --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> IO16
	IO22 --> ordeq_dev_tools.pipelines.generate_release_notes:tags
	ordeq_dev_tools.pipelines.generate_release_notes:tags --> IO24
	ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> IO25
	IO25 --> ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
	ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> IO26
	IO27 --> ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> IO28
	IO27 --> ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
	ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> IO29
	IO30 --> ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> IO27
	IO26 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	IO28 --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> IO31
	ordeq_dev_tools.pipelines.shared:packages --> IO0
	ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> IO32

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
		ordeq_dev_tools.pipelines.generate_draft_releases:create_releases@{shape: rounded, label: "create_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases@{shape: rounded, label: "draft_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:new_releases@{shape: rounded, label: "new_releases"}
		IO7@{shape: rect, label: "&lt;anonymous&gt;"}
		IO8@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s3["ordeq_dev_tools.pipelines.generate_release_notes"]
		direction TB
		ordeq_dev_tools.pipelines.generate_release_notes:bump_type@{shape: rounded, label: "bump_type"}
		ordeq_dev_tools.pipelines.generate_release_notes:bump_version@{shape: rounded, label: "bump_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:changes@{shape: rounded, label: "changes"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files@{shape: rounded, label: "commit_changed_files"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes@{shape: rounded, label: "commit_hashes"}
		ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag@{shape: rounded, label: "commits_since_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes@{shape: rounded, label: "create_release_notes"}
		ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels@{shape: rounded, label: "distinct_labels"}
		ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag@{shape: rounded, label: "get_new_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_tag@{shape: rounded, label: "latest_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_version@{shape: rounded, label: "latest_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits@{shape: rounded, label: "relevant_commits"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs@{shape: rounded, label: "relevant_prs"}
		ordeq_dev_tools.pipelines.generate_release_notes:tags@{shape: rounded, label: "tags"}
		IO10@{shape: rect, label: "&lt;anonymous&gt;"}
		IO11@{shape: rect, label: "&lt;anonymous&gt;"}
		IO12@{shape: rect, label: "&lt;anonymous&gt;"}
		IO13@{shape: rect, label: "&lt;anonymous&gt;"}
		IO14@{shape: rect, label: "&lt;anonymous&gt;"}
		IO15@{shape: rect, label: "&lt;anonymous&gt;"}
		IO16@{shape: rect, label: "&lt;anonymous&gt;"}
		IO17@{shape: rect, label: "&lt;anonymous&gt;"}
		IO18@{shape: rect, label: "&lt;anonymous&gt;"}
		IO19@{shape: rect, label: "&lt;anonymous&gt;"}
		IO20@{shape: rect, label: "&lt;anonymous&gt;"}
		IO24@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s4["ordeq_dev_tools.pipelines.list_changed_packages"]
		direction TB
		ordeq_dev_tools.pipelines.list_changed_packages:changed_files@{shape: rounded, label: "changed_files"}
		ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages@{shape: rounded, label: "extract_changed_packages"}
		IO25@{shape: rect, label: "&lt;anonymous&gt;"}
	end
	subgraph s5["ordeq_dev_tools.pipelines.list_dependencies"]
		direction TB
		ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies@{shape: rounded, label: "compute_affected_dependencies"}
		ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram@{shape: rounded, label: "generate_mermaid_diagram"}
		ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies@{shape: rounded, label: "parse_dependencies"}
		IO27@{shape: rect, label: "dependencies"}
	end
	subgraph s6["ordeq_dev_tools.pipelines.relevant_packages"]
		direction TB
		ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages@{shape: rounded, label: "extract_relevant_packages"}
	end
	subgraph s7["ordeq_dev_tools.pipelines.shared"]
		direction TB
		ordeq_dev_tools.pipelines.shared:packages@{shape: rounded, label: "packages"}
	end
	subgraph s8["ordeq_dev_tools.pipelines.viz_self"]
		direction TB
		ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools@{shape: rounded, label: "visualize_ordeq_dev_tools"}
	end
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO2@{shape: rect, label: "package_overview"}
	IO21@{shape: rect, label: "release_notes"}
	IO22@{shape: rect, label: "package"}
	IO23@{shape: rect, label: "new_tag"}
	IO26@{shape: rect, label: "packages"}
	IO28@{shape: rect, label: "affected_dependencies"}
	IO29@{shape: rect, label: "diagram"}
	IO30@{shape: rect, label: "lock_file"}
	IO31@{shape: rect, label: "relevant_packages"}
	IO32@{shape: rect, label: "ordeq_dev_tools_diagram"}
	IO5@{shape: rect, label: "docs_file"}
	IO6@{shape: rect, label: "updated_docs_file"}
	IO9@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,ordeq_dev_tools.pipelines.docs_package_overview:groups,ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group,ordeq_dev_tools.pipelines.docs_update_just:docs_just_section,ordeq_dev_tools.pipelines.docs_update_just:just_output,ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section,ordeq_dev_tools.pipelines.generate_draft_releases:create_releases,ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases,ordeq_dev_tools.pipelines.generate_draft_releases:new_releases,ordeq_dev_tools.pipelines.generate_release_notes:bump_type,ordeq_dev_tools.pipelines.generate_release_notes:bump_version,ordeq_dev_tools.pipelines.generate_release_notes:changes,ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files,ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes,ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag,ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes,ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels,ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag,ordeq_dev_tools.pipelines.generate_release_notes:latest_tag,ordeq_dev_tools.pipelines.generate_release_notes:latest_version,ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits,ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs,ordeq_dev_tools.pipelines.generate_release_notes:tags,ordeq_dev_tools.pipelines.list_changed_packages:changed_files,ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages,ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies,ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram,ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies,ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages,ordeq_dev_tools.pipelines.shared:packages,ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools node
	class L00,IO1,IO3,IO4,IO7,IO8,IO10,IO11,IO12,IO13,IO14,IO15,IO16,IO17,IO18,IO19,IO20,IO24,IO25,IO0,IO21,IO23,IO9 io0
	class L01,IO22 io1
	class L02,IO27,IO26,IO28,IO31 io2
	class L03,IO30 io3
	class L04,IO29,IO32,IO5,IO6 io4
	class L05,IO2 io5
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
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