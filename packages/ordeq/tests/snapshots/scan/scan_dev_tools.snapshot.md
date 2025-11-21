## Resource

```python
from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(ordeq_dev_tools))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function write_html_table_by_group at HASH1>: ('ordeq_dev_tools.pipelines.docs_package_overview', 'write_html_table_by_group'),
 <function groups at HASH2>: ('ordeq_dev_tools.pipelines.docs_package_overview', 'groups'),
 <function just_output at HASH3>: ('ordeq_dev_tools.pipelines.docs_update_just', 'just_output'),
 <function docs_just_section at HASH4>: ('ordeq_dev_tools.pipelines.docs_update_just', 'docs_just_section'),
 <function update_docs_with_just_section at HASH5>: ('ordeq_dev_tools.pipelines.docs_update_just', 'update_docs_with_just_section'),
 <function packages at HASH6>: ('ordeq_dev_tools.pipelines.validate_pyproject', 'packages'),
 <function tags at HASH7>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'tags'),
 <function latest_tag at HASH8>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_tag'),
 <function latest_version at HASH9>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'latest_version'),
 <function commits_since_tag at HASH10>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'commits_since_tag'),
 <function commit_hashes at HASH11>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_hashes'),
 <function commit_changed_files at HASH12>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'commit_changed_files'),
 <function relevant_commits at HASH13>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_commits'),
 <function relevant_prs at HASH14>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'relevant_prs'),
 <function distinct_labels at HASH15>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'distinct_labels'),
 <function bump_type at HASH16>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_type'),
 <function bump_version at HASH17>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'bump_version'),
 <function get_new_tag at HASH18>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'get_new_tag'),
 <function changes at HASH19>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'changes'),
 <function create_release_notes at HASH20>: ('ordeq_dev_tools.pipelines.generate_release_notes', 'create_release_notes'),
 <function draft_releases at HASH21>: ('ordeq_dev_tools.pipelines.generate_draft_releases', 'draft_releases'),
 <function new_releases at HASH22>: ('ordeq_dev_tools.pipelines.generate_draft_releases', 'new_releases'),
 <function create_releases at HASH23>: ('ordeq_dev_tools.pipelines.generate_draft_releases', 'create_releases'),
 <function changed_files at HASH24>: ('ordeq_dev_tools.pipelines.list_changed_packages', 'changed_files'),
 <function extract_changed_packages at HASH25>: ('ordeq_dev_tools.pipelines.list_changed_packages', 'extract_changed_packages'),
 <function parse_dependencies at HASH26>: ('ordeq_dev_tools.pipelines.list_dependencies', 'parse_dependencies'),
 <function generate_mermaid_diagram at HASH27>: ('ordeq_dev_tools.pipelines.list_dependencies', 'generate_mermaid_diagram'),
 <function compute_affected_dependencies at HASH28>: ('ordeq_dev_tools.pipelines.list_dependencies', 'compute_affected_dependencies'),
 <function extract_relevant_packages at HASH29>: ('ordeq_dev_tools.pipelines.relevant_packages', 'extract_relevant_packages'),
 <function groups at HASH30>: ('ordeq_dev_tools.pipelines.validate_pyproject', 'groups'),
 <function visualize_ordeq_dev_tools at HASH31>: ('ordeq_dev_tools.pipelines.viz_self', 'visualize_ordeq_dev_tools')}
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