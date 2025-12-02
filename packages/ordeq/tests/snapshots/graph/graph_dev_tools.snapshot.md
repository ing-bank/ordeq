## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import ordeq_dev_tools
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(ordeq_dev_tools)
nodes_and_views = _collect_views(*fqn_nodes)
base_graph = NodeIOGraph.from_nodes(nodes_and_views)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes_and_views)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

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
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> io-8
io-7 --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
io-7 --> View:ordeq_dev_tools.pipelines.generate_release_notes:changes
io-8 --> View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages
io-8 --> View:ordeq_dev_tools.pipelines.docs_package_overview:groups
io-8 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
io-8 --> View:ordeq_dev_tools.pipelines.validate_pyproject:groups
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> io-9
View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages --> io-10
io-9 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
io-10 --> View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> io-11
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> io-12
View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages --> io-13
View:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...) --> io-14
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...) --> io-15
io-11 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-12 --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
io-13 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
io-14 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
io-15 --> View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> io-16
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...) --> io-21
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> io-22
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...) --> io-23
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> io-24
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs --> io-25
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> io-26
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> io-28
io-16 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
io-17 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-18 --> Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
io-19 --> Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
io-19 --> Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
io-20 --> Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
io-21 --> Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
io-22 --> Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
io-23 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-24 --> View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
io-25 --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes
io-26 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-27 --> Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
io-28 --> Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag --> io-29
View:ordeq_dev_tools.pipelines.validate_pyproject:groups --> io-30
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages --> io-31
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram --> io-32
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies --> io-33
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies --> io-34
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages --> io-35
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes --> io-36
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases --> io-37
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes --> io-38
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section --> io-39
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group --> io-40
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools --> io-41
Node:ordeq_dev_tools.pipelines.generate_gallery:generate_gallery --> io-42
NodeGraph
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> View:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> View:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
View:ordeq_dev_tools.pipelines.generate_release_notes:tags --> View:ordeq_dev_tools.pipelines.generate_release_notes:tags
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag --> View:ordeq_dev_tools.pipelines.generate_release_notes:commits_since_tag
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_hashes
View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files --> View:ordeq_dev_tools.pipelines.generate_release_notes:commit_changed_files
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_commits
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...)
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...)
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...)
View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...) --> View:View(func=ordeq_dev_tools.pipelines.shared:packages, ...)
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs --> View:ordeq_dev_tools.pipelines.generate_release_notes:relevant_prs
View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages --> View:ordeq_dev_tools.pipelines.generate_api_docs:filter_packages
View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels --> View:ordeq_dev_tools.pipelines.generate_release_notes:distinct_labels
View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...) --> View:View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output, ...)
View:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...) --> View:View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs, ...)
View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages --> View:ordeq_dev_tools.pipelines.generate_api_docs:check_ios_packages
View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version --> View:ordeq_dev_tools.pipelines.generate_release_notes:latest_version
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type --> View:ordeq_dev_tools.pipelines.generate_release_notes:bump_type
View:ordeq_dev_tools.pipelines.docs_package_overview:groups --> Node:ordeq_dev_tools.pipelines.docs_package_overview:groups
View:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section --> Node:ordeq_dev_tools.pipelines.docs_update_just:docs_just_section
Loader:Loader(func=ordeq_files.text:load, ...) --> Node:Loader(func=ordeq_files.text:load, ...)
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs --> View:ordeq_dev_tools.pipelines.generate_api_docs:generate_package_docs
View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...) --> View:View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases, ...)
View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases --> View:ordeq_dev_tools.pipelines.generate_draft_releases:new_releases
View:ordeq_dev_tools.pipelines.generate_release_notes:changes --> Node:ordeq_dev_tools.pipelines.generate_release_notes:changes
View:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...) --> Node:View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files, ...)
Loader:Loader(func=ordeq_toml.toml:load, ...) --> Node:Loader(func=ordeq_toml.toml:load, ...)
Loader:Loader(func=ordeq_files.json:load, ...) --> Node:Loader(func=ordeq_files.json:load, ...)
Loader:Loader(func=ordeq_files.json:load, ...) --> Node:Loader(func=ordeq_files.json:load, ...)
Loader:Loader(func=ordeq_files.json:load, ...) --> Node:Loader(func=ordeq_files.json:load, ...)
Loader:Loader(func=ordeq_files.json:load, ...) --> Node:Loader(func=ordeq_files.json:load, ...)
View:ordeq_dev_tools.pipelines.generate_release_notes:bump_version --> Node:ordeq_dev_tools.pipelines.generate_release_notes:bump_version
Node:ordeq_dev_tools.pipelines.generate_gallery:generate_gallery
Node:ordeq_dev_tools.pipelines.viz_self:visualize_ordeq_dev_tools
Node:ordeq_dev_tools.pipelines.docs_package_overview:write_html_table_by_group
Node:ordeq_dev_tools.pipelines.docs_update_just:update_docs_with_just_section
View:ordeq_dev_tools.pipelines.generate_api_docs:generate_api_readmes
View:ordeq_dev_tools.pipelines.generate_draft_releases:create_releases
Node:ordeq_dev_tools.pipelines.generate_release_notes:create_release_notes
Node:ordeq_dev_tools.pipelines.list_changed_packages:extract_changed_packages
Node:ordeq_dev_tools.pipelines.list_dependencies:parse_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:compute_affected_dependencies
Node:ordeq_dev_tools.pipelines.list_dependencies:generate_mermaid_diagram
Node:ordeq_dev_tools.pipelines.relevant_packages:extract_relevant_packages
View:ordeq_dev_tools.pipelines.validate_pyproject:groups
Node:ordeq_dev_tools.pipelines.generate_release_notes:get_new_tag
Topological ordering
(Loader(func=<bound method _raise_not_implemented of Input(id=ID1)>,
        inputs=(),
        outputs=(IO(id=ID2),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=Input(id=ID1)),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=tags, inputs=[IO(id=ID2)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_tag, inputs=[IO(id=ID3)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commits_since_tag, inputs=[IO(id=ID4)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_hashes, inputs=[IO(id=ID5)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=commit_changed_files, inputs=[IO(id=ID6)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_commits, inputs=[IO(id=ID6), IO(id=ID7), IO(id=ID2)]),
 View(func=ordeq_dev_tools.pipelines.shared:packages),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=relevant_prs, inputs=[IO(id=ID8)]),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=filter_packages, inputs=[IO(id=ID9)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=distinct_labels, inputs=[IO(id=ID10)]),
 View(func=ordeq_dev_tools.pipelines.docs_update_just:just_output),
 View(func=ordeq_dev_tools.pipelines.generate_api_docs:clear_api_docs),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=check_ios_packages, inputs=[IO(id=ID11)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=latest_version, inputs=[IO(id=ID4)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_type, inputs=[IO(id=ID12)]),
 View(module=ordeq_dev_tools.pipelines.docs_package_overview, name=groups, inputs=[IO(id=ID9)]),
 View(module=ordeq_dev_tools.pipelines.docs_update_just, name=docs_just_section, inputs=[IO(id=ID13)]),
 Loader(func=<bound method Text.load of Text(path=Path('/docs/CONTRIBUTING.md'))>,
        inputs=(),
        outputs=(IO(id=ID14),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=Text(path=Path('/docs/CONTRIBUTING.md'))),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=generate_package_docs, inputs=[IO(id=ID15), IO(id=ID16)]),
 View(func=ordeq_dev_tools.pipelines.generate_draft_releases:draft_releases),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=new_releases, inputs=[IO(id=ID9)]),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=changes, inputs=[IO(id=ID8), IO(id=ID5), IO(id=ID10)]),
 View(func=ordeq_dev_tools.pipelines.list_changed_packages:changed_files),
 Loader(func=<bound method TOML.load of TOML(path=Path('/uv.lock'))>,
        inputs=(),
        outputs=(IO(id=ID17),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=TOML(path=Path('/uv.lock'))),
 Loader(func=<bound method JSON.load of JSON(path=Path('/data/dev_tools/dependencies.json'))>,
        inputs=(),
        outputs=(IO(id=ID18),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=JSON(path=Path('/data/dev_tools/dependencies.json'))),
 Loader(func=<bound method JSON.load of JSON(path=Path('/data/dev_tools/changed_packages.json'))>,
        inputs=(),
        outputs=(IO(id=ID19),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=JSON(path=Path('/data/dev_tools/changed_packages.json'))),
 Loader(func=<bound method JSON.load of JSON(path=Path('/data/dev_tools/affected_dependencies.json'))>,
        inputs=(),
        outputs=(IO(id=ID20),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=JSON(path=Path('/data/dev_tools/affected_dependencies.json'))),
 View(module=ordeq_dev_tools.pipelines.generate_release_notes, name=bump_version, inputs=[IO(id=ID21), IO(id=ID22)]),
 Node(module=ordeq_dev_tools.pipelines.generate_gallery, name=generate_gallery, outputs=[Text(path=Path('/docs/guides/gallery.md'))]),
 Node(module=ordeq_dev_tools.pipelines.viz_self, name=visualize_ordeq_dev_tools, outputs=[Text(path=Path('/data/dev_tools/ordeq_dev_tools_diagram.mmd'))]),
 Node(module=ordeq_dev_tools.pipelines.docs_package_overview, name=write_html_table_by_group, inputs=[IO(id=ID23)], outputs=[TextLinesStream(path=Path('/docs/packages.md'))]),
 Node(module=ordeq_dev_tools.pipelines.docs_update_just, name=update_docs_with_just_section, inputs=[IO(id=ID14), IO(id=ID24)], outputs=[Text(path=Path('/docs/CONTRIBUTING.md'))]),
 View(module=ordeq_dev_tools.pipelines.generate_api_docs, name=generate_api_readmes, inputs=[IO(id=ID25)]),
 View(module=ordeq_dev_tools.pipelines.generate_draft_releases, name=create_releases, inputs=[IO(id=ID26), IO(id=ID27)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=create_release_notes, inputs=[IO(id=ID28)], outputs=[IO(id=ID29)]),
 Node(module=ordeq_dev_tools.pipelines.list_changed_packages, name=extract_changed_packages, inputs=[IO(id=ID30)], outputs=[JSON(path=Path('/data/dev_tools/changed_packages.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=parse_dependencies, inputs=[IO(id=ID17)], outputs=[JSON(path=Path('/data/dev_tools/dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=compute_affected_dependencies, inputs=[IO(id=ID18)], outputs=[JSON(path=Path('/data/dev_tools/affected_dependencies.json'))]),
 Node(module=ordeq_dev_tools.pipelines.list_dependencies, name=generate_mermaid_diagram, inputs=[IO(id=ID18)], outputs=[Text(path=Path('/data/dev_tools/dependencies_diagram.mmd'))]),
 Node(module=ordeq_dev_tools.pipelines.relevant_packages, name=extract_relevant_packages, inputs=[IO(id=ID19), IO(id=ID20)], outputs=[JSON(path=Path('/data/dev_tools/relevant_packages.json'))]),
 View(module=ordeq_dev_tools.pipelines.validate_pyproject, name=groups, inputs=[IO(id=ID9)]),
 Node(module=ordeq_dev_tools.pipelines.generate_release_notes, name=get_new_tag, inputs=[IO(id=ID2), IO(id=ID31)], outputs=[IO(id=ID32)]))

```

## Logging

```text
WARNING	ordeq.preview	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.

```