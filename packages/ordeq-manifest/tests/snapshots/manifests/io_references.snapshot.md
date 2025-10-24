## Resource

```python
from ordeq_manifest import create_manifest_json
import example2

print(create_manifest_json(example2))

```

## Output

```text
{
  "name": "example2",
  "nodes": {},
  "ios": {
    "example2.io_references.nested_test_io": {
      "id": "example2.io_references.nested_test_io",
      "name": "nested_test_io",
      "type": "example2.io_references.MyIO",
      "references": [
        "other_io"
      ]
    },
    "example2.io_references.test_io": {
      "id": "example2.io_references.test_io",
      "name": "test_io",
      "type": "example2.io_references.MyIO",
      "references": [
        "other_io"
      ]
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/io_references.py:2: error: Skipping analyzing "example2": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/io_references.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```