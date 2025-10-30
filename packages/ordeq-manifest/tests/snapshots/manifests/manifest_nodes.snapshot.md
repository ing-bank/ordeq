## Resource

```python
from ordeq_manifest import create_manifest_json
from example_project import nodes

print(create_manifest_json(nodes))

```

## Output

```text
{
  "name": "example_project.nodes",
  "nodes": {
    "example_project.nodes:func": {
      "id": "example_project.nodes:func",
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
      "id": "example_project.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes:y": {
      "id": "example_project.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/manifest_nodes.py:2: error: Skipping analyzing "example_project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/manifest_nodes.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```