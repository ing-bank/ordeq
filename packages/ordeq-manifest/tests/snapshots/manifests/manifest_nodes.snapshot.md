## Resource

```python
from example_project import nodes
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes))

```

## Output

```text
{
  "name": "example_project.nodes",
  "nodes": {
    "example_project.nodes:func": {
      "name": "func",
      "inputs": [
        "example_project.nodes:x"
      ],
      "outputs": [
        "example_project.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "example_project.nodes:x": {
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes:y": {
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```