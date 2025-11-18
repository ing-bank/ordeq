## Resource

```python
from example_project import inner
from ordeq_manifest import create_manifest_json

print(create_manifest_json(inner))

```

## Output

```text
{
  "name": "example_project.inner",
  "nodes": {
    "example_project.inner.nodes:func": {
      "name": "func",
      "inputs": [
        "example_project.inner.nodes:x"
      ],
      "outputs": [
        "example_project.inner.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "example_project.inner.nodes:x": {
      "name": "x",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.inner.nodes:y": {
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    }
  },
  "resources": []
}

```