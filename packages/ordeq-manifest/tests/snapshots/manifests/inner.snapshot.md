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
      "id": "example_project.inner.nodes:func",
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
      "id": "example_project.inner.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.inner.nodes:y": {
      "id": "example_project.inner.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/inner.py:1: error: Skipping analyzing "example_project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/inner.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```