## Resource

```python
import ordeq_dev_tools

from ordeq_viz import viz

diagram = viz(ordeq_dev_tools, fmt="mermaid", subgraphs=True)
print(diagram)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
		io_type_2@{shape: rect, label: "JSON"}
		io_type_3@{shape: rect, label: "TOML"}
		io_type_4@{shape: rect, label: "Text"}
		io_type_5@{shape: rect, label: "TextLinesStream"}
	end

	ordeq_dev_tools.pipelines.generate_release_notes:package --> ordeq_dev_tools.pipelines.generate_release_notes:tags
	ordeq_dev_tools.pipelines.generate_release_notes:tags --> ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
	ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
	ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
	ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
	ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:package --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
	ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> ordeq_dev_tools.pipelines.generate_release_notes:latest_version
	ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> ordeq_dev_tools.pipelines.generate_release_notes:bump_type
	ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> ordeq_dev_tools.pipelines.generate_release_notes:bump_version
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> ordeq_dev_tools.pipelines.generate_release_notes:changes
	ordeq_dev_tools.pipelines.generate_release_notes:package --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> ordeq_dev_tools.pipelines.generate_release_notes:new_tag
	ordeq_dev_tools.pipelines.generate_release_notes:changes --> ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
	ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> ordeq_dev_tools.pipelines.generate_release_notes:release_notes
	ordeq_dev_tools.pipelines.docs_update_just:just_output --> ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
	ordeq_dev_tools.pipelines.docs_update_just:docs_file --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
	ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> ordeq_dev_tools.pipelines.docs_update_just:updated_docs_file
	ordeq_dev_tools.pipelines.shared:packages --> ordeq_dev_tools.pipelines.docs_package_overview:groups
	ordeq_dev_tools.pipelines.docs_package_overview:groups --> ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
	ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> ordeq_dev_tools.pipelines.docs_package_overview:package_overview
	ordeq_dev_tools.pipelines.shared:packages --> ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases --> ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
	ordeq_dev_tools.pipelines.list_changed_packages:changed_files --> ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
	ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> ordeq_dev_tools.pipelines.list_changed_packages:changed_packages
	ordeq_dev_tools.pipelines.list_dependencies:lock_file --> ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> ordeq_dev_tools.pipelines.list_dependencies:dependencies
	ordeq_dev_tools.pipelines.list_dependencies:dependencies --> ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> ordeq_dev_tools.pipelines.list_dependencies:affected_dependencies
	ordeq_dev_tools.pipelines.list_dependencies:dependencies --> ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
	ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> ordeq_dev_tools.pipelines.list_dependencies:diagram
	ordeq_dev_tools.pipelines.relevant_packages:packages --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	ordeq_dev_tools.pipelines.relevant_packages:affected_dependencies --> ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
	ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> ordeq_dev_tools.pipelines.relevant_packages:relevant_packages
	ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> ordeq_dev_tools.pipelines.viz_self:ordeq_dev_tools_diagram
	ordeq_dev_tools.pipelines.shared:packages --> ordeq_dev_tools.pipelines.validate_pyproject:groups

	subgraph s0["ordeq_dev_tools.pipelines.generate_release_notes"]
		direction TB
		ordeq_dev_tools.pipelines.generate_release_notes:tags@{shape: subroutine, label: "tags"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_tag@{shape: subroutine, label: "latest_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag@{shape: subroutine, label: "commits_since_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes@{shape: subroutine, label: "commit_hashes"}
		ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files@{shape: subroutine, label: "commit_changed_files"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits@{shape: subroutine, label: "relevant_commits"}
		ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs@{shape: subroutine, label: "relevant_prs"}
		ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels@{shape: subroutine, label: "distinct_labels"}
		ordeq_dev_tools.pipelines.generate_release_notes:latest_version@{shape: subroutine, label: "latest_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:bump_type@{shape: subroutine, label: "bump_type"}
		ordeq_dev_tools.pipelines.generate_release_notes:bump_version@{shape: subroutine, label: "bump_version"}
		ordeq_dev_tools.pipelines.generate_release_notes:changes@{shape: subroutine, label: "changes"}
		ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag@{shape: rounded, label: "get_new_tag"}
		ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes@{shape: rounded, label: "create_release_notes"}
	end
	subgraph s1["ordeq_dev_tools.pipelines.shared"]
		direction TB
		ordeq_dev_tools.pipelines.shared:packages@{shape: subroutine, label: "packages"}
	end
	subgraph s2["ordeq_dev_tools.pipelines.docs_update_just"]
		direction TB
		ordeq_dev_tools.pipelines.docs_update_just:just_output@{shape: subroutine, label: "just_output"}
		ordeq_dev_tools.pipelines.docs_update_just:docs_just_section@{shape: subroutine, label: "docs_just_section"}
		ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section@{shape: rounded, label: "update_docs_with_just_section"}
	end
	subgraph s3["ordeq_dev_tools.pipelines.docs_package_overview"]
		direction TB
		ordeq_dev_tools.pipelines.docs_package_overview:groups@{shape: subroutine, label: "groups"}
		ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group@{shape: rounded, label: "write_html_table_by_group"}
	end
	subgraph s4["ordeq_dev_tools.pipelines.generate_draft_releases"]
		direction TB
		ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases@{shape: subroutine, label: "draft_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:new_releases@{shape: subroutine, label: "new_releases"}
		ordeq_dev_tools.pipelines.generate_draft_releases:create_releases@{shape: subroutine, label: "create_releases"}
	end
	subgraph s5["ordeq_dev_tools.pipelines.list_changed_packages"]
		direction TB
		ordeq_dev_tools.pipelines.list_changed_packages:changed_files@{shape: subroutine, label: "changed_files"}
		ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages@{shape: rounded, label: "extract_changed_packages"}
	end
	subgraph s6["ordeq_dev_tools.pipelines.list_dependencies"]
		direction TB
		ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies@{shape: rounded, label: "parse_dependencies"}
		ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies@{shape: rounded, label: "compute_affected_dependencies"}
		ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram@{shape: rounded, label: "generate_mermaid_diagram"}
		ordeq_dev_tools.pipelines.list_dependencies:dependencies@{shape: rect, label: "dependencies"}
	end
	subgraph s7["ordeq_dev_tools.pipelines.relevant_packages"]
		direction TB
		ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages@{shape: rounded, label: "extract_relevant_packages"}
	end
	subgraph s8["ordeq_dev_tools.pipelines.viz_self"]
		direction TB
		ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools@{shape: rounded, label: "visualize_ordeq_dev_tools"}
	end
	subgraph s9["ordeq_dev_tools.pipelines.validate_pyproject"]
		direction TB
		ordeq_dev_tools.pipelines.validate_pyproject:groups@{shape: subroutine, label: "groups"}
	end
	ordeq_dev_tools.pipelines.docs_package_overview:package_overview@{shape: rect, label: "package_overview"}
	ordeq_dev_tools.pipelines.docs_update_just:docs_file@{shape: rect, label: "docs_file"}
	ordeq_dev_tools.pipelines.docs_update_just:updated_docs_file@{shape: rect, label: "updated_docs_file"}
	ordeq_dev_tools.pipelines.generate_release_notes:new_tag@{shape: rect, label: "new_tag"}
	ordeq_dev_tools.pipelines.generate_release_notes:package@{shape: rect, label: "package"}
	ordeq_dev_tools.pipelines.generate_release_notes:release_notes@{shape: rect, label: "release_notes"}
	ordeq_dev_tools.pipelines.list_changed_packages:changed_packages@{shape: rect, label: "changed_packages"}
	ordeq_dev_tools.pipelines.list_dependencies:affected_dependencies@{shape: rect, label: "affected_dependencies"}
	ordeq_dev_tools.pipelines.list_dependencies:diagram@{shape: rect, label: "diagram"}
	ordeq_dev_tools.pipelines.list_dependencies:lock_file@{shape: rect, label: "lock_file"}
	ordeq_dev_tools.pipelines.relevant_packages:affected_dependencies@{shape: rect, label: "affected_dependencies"}
	ordeq_dev_tools.pipelines.relevant_packages:packages@{shape: rect, label: "packages"}
	ordeq_dev_tools.pipelines.relevant_packages:relevant_packages@{shape: rect, label: "relevant_packages"}
	ordeq_dev_tools.pipelines.viz_self:ordeq_dev_tools_diagram@{shape: rect, label: "ordeq_dev_tools_diagram"}

	class node_type,ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag,ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes,ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section,ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group,ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages,ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies,ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies,ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram,ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages,ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools node
	class view_type,ordeq_dev_tools.pipelines.generate_release_notes:tags,ordeq_dev_tools.pipelines.generate_release_notes:latest_tag,ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag,ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes,ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files,ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits,ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs,ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels,ordeq_dev_tools.pipelines.generate_release_notes:latest_version,ordeq_dev_tools.pipelines.generate_release_notes:bump_type,ordeq_dev_tools.pipelines.generate_release_notes:bump_version,ordeq_dev_tools.pipelines.generate_release_notes:changes,ordeq_dev_tools.pipelines.shared:packages,ordeq_dev_tools.pipelines.docs_update_just:just_output,ordeq_dev_tools.pipelines.docs_update_just:docs_just_section,ordeq_dev_tools.pipelines.docs_package_overview:groups,ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases,ordeq_dev_tools.pipelines.generate_draft_releases:new_releases,ordeq_dev_tools.pipelines.generate_draft_releases:create_releases,ordeq_dev_tools.pipelines.list_changed_packages:changed_files,ordeq_dev_tools.pipelines.validate_pyproject:groups view
	class io_type_0,ordeq_dev_tools.pipelines.generate_release_notes:new_tag,ordeq_dev_tools.pipelines.generate_release_notes:release_notes io0
	class io_type_1,ordeq_dev_tools.pipelines.generate_release_notes:package io1
	class io_type_2,ordeq_dev_tools.pipelines.list_dependencies:dependencies,ordeq_dev_tools.pipelines.list_changed_packages:changed_packages,ordeq_dev_tools.pipelines.list_dependencies:affected_dependencies,ordeq_dev_tools.pipelines.relevant_packages:affected_dependencies,ordeq_dev_tools.pipelines.relevant_packages:packages,ordeq_dev_tools.pipelines.relevant_packages:relevant_packages io2
	class io_type_3,ordeq_dev_tools.pipelines.list_dependencies:lock_file io3
	class io_type_4,ordeq_dev_tools.pipelines.docs_update_just:docs_file,ordeq_dev_tools.pipelines.docs_update_just:updated_docs_file,ordeq_dev_tools.pipelines.list_dependencies:diagram,ordeq_dev_tools.pipelines.viz_self:ordeq_dev_tools_diagram io4
	class io_type_5,ordeq_dev_tools.pipelines.docs_package_overview:package_overview io5
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

## Warnings

```text
UserWarning: View(func=ordeq_dev_tools.pipelines.shared:packages, ...) was provided more than once. Duplicates are ignored.
```

## Logging

```text
WARNING	ordeq.preview	Subgraphs are in pre-release, functionality may break in future releases without it being considered a breaking change.

```