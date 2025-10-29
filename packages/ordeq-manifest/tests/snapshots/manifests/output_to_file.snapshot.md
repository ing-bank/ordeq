## Resource

```python
from tempfile import NamedTemporaryFile

from ordeq_manifest import create_manifest_json
from project import inner
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
  "name": "project.inner",
  "nodes": {
    "project.inner.nodes:func": {
      "id": "project.inner.nodes:func",
      "name": "func",
      "inputs": [
        "project.inner.nodes:x"
      ],
      "outputs": [
        "project.inner.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    }
  },
  "ios": {
    "project.inner.nodes:x": {
      "id": "project.inner.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "project.inner.nodes:y": {
      "id": "project.inner.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/output_to_file.py:4: error: Module "project" has no attribute "inner"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```