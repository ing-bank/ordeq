## Resource

```python
from pathlib import Path
from tempfile import NamedTemporaryFile

from example_project import inner
from ordeq_manifest import create_manifest_json

with NamedTemporaryFile() as file:
    path = Path(file.name)
    create_manifest_json(inner, output=path)
    print(path.read_text(encoding="utf8"))

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
      "checks": [],
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