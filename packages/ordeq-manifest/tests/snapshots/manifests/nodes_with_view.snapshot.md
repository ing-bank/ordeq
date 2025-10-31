## Resource

```python
from example_project import nodes_with_view
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes_with_view))

```

## Output

```text
{
  "name": "example_project.nodes_with_view",
  "nodes": {
    "example_project.nodes_with_view:farewell": {
      "id": "example_project.nodes_with_view:farewell",
      "name": "farewell",
      "inputs": [
        "example_project.nodes_with_view:greeting"
      ],
      "outputs": [
        "example_project.nodes_with_view:printer"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_project.nodes_with_view:<anonymous0>": {
      "id": "example_project.nodes_with_view:<anonymous0>",
      "name": "<anonymous0>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes_with_view:greeting": {
      "id": "example_project.nodes_with_view:greeting",
      "name": "greeting",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_with_view:printer": {
      "id": "example_project.nodes_with_view:printer",
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```