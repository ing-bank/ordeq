## Resource

```python
from ordeq_manifest import create_manifest_json
from project import nodes

print(create_manifest_json(nodes))

```

## Output

```text
{
  "name": "project.nodes",
  "nodes": {
    "project.nodes:func": {
      "id": "project.nodes:func",
      "name": "func",
      "inputs": [
        "project.nodes:x"
      ],
      "outputs": [
        "project.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "project.nodes:x": {
      "id": "project.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "project.nodes:y": {
      "id": "project.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/manifest_nodes.py:2: error: Module "project" has no attribute "nodes"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```