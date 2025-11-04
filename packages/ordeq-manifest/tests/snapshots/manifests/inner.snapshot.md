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
  "modules": [
    {
      "name": "example_project.inner.nodes",
      "nodes": {
        "func": "example_project.inner.nodes:func"
      },
      "ios": {
        "x": "io-0",
        "y": "io-1"
      }
    }
  ],
  "nodes": {
    "example_project.inner.nodes:func": {
      "inputs": [
        "io-0"
      ],
      "outputs": [
        "io-1"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      },
      "view": false
    }
  },
  "ios": {
    "io-0": {
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-1": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    }
  }
}

```