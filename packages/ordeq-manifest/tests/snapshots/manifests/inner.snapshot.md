## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import inner

print(create_manifest_json(inner))

```

## Output

```text
{
  "name": "examples.project.inner",
  "nodes": {
    "examples.project.inner.nodes:func": {
      "id": "examples.project.inner.nodes:func",
      "name": "func",
      "inputs": [
        "examples.project.inner.nodes:x"
      ],
      "outputs": [
        "examples.project.inner.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "examples.project.inner.nodes:x": {
      "id": "examples.project.inner.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "examples.project.inner.nodes:y": {
      "id": "examples.project.inner.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/inner.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/inner.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```