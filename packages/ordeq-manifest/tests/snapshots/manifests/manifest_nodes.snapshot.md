## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import nodes

print(create_manifest_json(nodes))

```

## Output

```text
{
  "name": "examples.project.nodes",
  "nodes": {
    "nodes.examples.project.nodes:func": {
      "id": "nodes.examples.project.nodes:func",
      "name": "examples.project.nodes:func",
      "inputs": [
        "examples.project.nodes.x"
      ],
      "outputs": [
        "examples.project.nodes.y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "examples.project.nodes.x": {
      "id": "examples.project.nodes.x",
      "name": "x",
      "type": "ordeq._io.IO",
      "references": []
    },
    "examples.project.nodes.y": {
      "id": "examples.project.nodes.y",
      "name": "y",
      "type": "ordeq_common.io.printer.Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/manifest_nodes.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/manifest_nodes.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```