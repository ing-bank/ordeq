## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(ordeq_dev_tools))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('ordeq_dev_tools.pipelines.validate_pyproject', 'packages'),
 ('ordeq_dev_tools.pipelines.docs_package_overview', 'groups'),
 ('ordeq_dev_tools.pipelines.docs_package_overview', 'write_html_table_by_group'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'just_output'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'docs_just_section'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'update_docs_with_just_section'),
 ('ordeq_dev_tools.pipelines.generate_draft_releases', 'draft_releases'),
 ('ordeq_dev_tools.pipelines.generate_draft_releases', 'new_releases'),
 ('ordeq_dev_tools.pipelines.generate_draft_releases', 'create_releases'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'tags'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_tag'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_version'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'commits_since_tag'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_hashes'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_changed_files'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_commits'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_prs'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'distinct_labels'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_type'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_version'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'get_new_tag'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'changes'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'create_release_notes'),
 ('ordeq_dev_tools.pipelines.list_changed_packages', 'changed_files'),
 ('ordeq_dev_tools.pipelines.list_changed_packages', 'extract_changed_packages'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'parse_dependencies'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'generate_mermaid_diagram'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'compute_affected_dependencies'),
 ('ordeq_dev_tools.pipelines.relevant_packages', 'extract_relevant_packages'),
 ('ordeq_dev_tools.pipelines.validate_pyproject', 'groups'),
 ('ordeq_dev_tools.pipelines.viz_self', 'visualize_ordeq_dev_tools')]
IOs:
[('ordeq_dev_tools.pipelines.docs_package_overview', 'package_overview'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'contribution_guide'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'docs_file'),
 ('ordeq_dev_tools.pipelines.docs_update_just', 'updated_docs_file'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'package'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'release_notes'),
 ('ordeq_dev_tools.pipelines.generate_release_notes', 'new_tag'),
 ('ordeq_dev_tools.pipelines.list_changed_packages', 'changed_packages'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'lock_file'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'dependencies'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'diagram'),
 ('ordeq_dev_tools.pipelines.list_dependencies', 'affected_dependencies'),
 ('ordeq_dev_tools.pipelines.relevant_packages', 'affected_dependencies'),
 ('ordeq_dev_tools.pipelines.relevant_packages', 'packages'),
 ('ordeq_dev_tools.pipelines.relevant_packages', 'relevant_packages'),
 ('ordeq_dev_tools.pipelines.viz_self', 'ordeq_dev_tools_diagram')]

```