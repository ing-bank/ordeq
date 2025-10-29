## Resource

```python
from ordeq_manifest import create_manifest_json
from project import nodes_with_view

print(create_manifest_json(nodes_with_view))

```

## Output

```text
{
  "name": "project.nodes_with_view",
  "nodes": {
    "project.nodes_with_view:farewell": {
      "id": "project.nodes_with_view:farewell",
      "name": "farewell",
      "inputs": [
        "project.nodes_with_view:greeting"
      ],
      "outputs": [
        "project.nodes_with_view:printer"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "project.nodes_with_view:greeting": {
      "id": "project.nodes_with_view:greeting",
      "name": "greeting",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_with_view:printer": {
      "id": "project.nodes_with_view:printer",
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_with_view.py:2: error: Module "project" has no attribute "nodes_with_view"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```