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
      "name": "func",
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
      "name": "x",
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-1": {
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    }
  }
}

```