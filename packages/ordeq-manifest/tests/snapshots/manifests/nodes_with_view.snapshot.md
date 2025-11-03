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
  "modules": [
    {
      "name": "example_project.nodes_with_view",
      "nodes": {
        "farewell": "example_project.nodes_with_view:farewell",
        "greet": "example_project.nodes_with_view:greet"
      },
      "ios": {
        "printer": "io-0",
        "<anonymous0>": "io-1",
        "<anonymous1>": "io-2"
      }
    }
  ],
  "nodes": {
    "example_project.nodes_with_view:farewell": {
      "inputs": [
        "example_project.nodes_with_view:greet"
      ],
      "outputs": [
        "io-0"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_with_view:greet": {
      "inputs": [],
      "outputs": [
        "io-2"
      ],
      "attributes": {},
      "view": true
    }
  },
  "ios": {
    "io-0": {
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    },
    "io-1": {
      "name": "<anonymous0>",
      "type": "ordeq._nodes:View",
      "references": {}
    },
    "io-2": {
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "references": {}
    }
  }
}

```