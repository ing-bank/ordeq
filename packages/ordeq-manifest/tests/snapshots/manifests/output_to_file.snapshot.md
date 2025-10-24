## Resource

```python
from tempfile import NamedTemporaryFile

from ordeq_manifest import create_manifest_json
from examples.project import inner
from pathlib import Path

with NamedTemporaryFile() as file:
    path = Path(file.name)
    create_manifest_json(inner, output=path)
    print('JSON:/n', path.read_text())

```

## Output

```text
JSON:
 {
  "name": "examples.project.inner",
  "nodes": {
    "nodes.examples.project.inner.nodes:func": {
      "id": "nodes.examples.project.inner.nodes:func",
      "name": "examples.project.inner.nodes:func",
      "inputs": [
        "examples.project.inner.nodes.x"
      ],
      "outputs": [
        "examples.project.inner.nodes.y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "examples.project.inner.nodes.x": {
      "id": "examples.project.inner.nodes.x",
      "name": "x",
      "type": "ordeq._io.IO",
      "references": []
    },
    "examples.project.inner.nodes.y": {
      "id": "examples.project.inner.nodes.y",
      "name": "y",
      "type": "ordeq_common.io.printer.Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/output_to_file.py:4: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/output_to_file.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```