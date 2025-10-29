## Resource

```python
import references
from ordeq_manifest import create_manifest_json

print(create_manifest_json(references))

```

## Output

```text
{
  "name": "references",
  "nodes": {},
  "ios": {
    "references.io_references:named_nested_test_io": {
      "id": "references.io_references:named_nested_test_io",
      "name": "named_nested_test_io",
      "type": "references.io_references:MyIO",
      "references": [
        "other_io"
      ]
    },
    "references.io_references:named_test_io": {
      "id": "references.io_references:named_test_io",
      "name": "named_test_io",
      "type": "references.io_references:MyIO",
      "references": [
        "other_io"
      ]
    },
    "references.io_references:nested_test_io": {
      "id": "references.io_references:nested_test_io",
      "name": "nested_test_io",
      "type": "references.io_references:MyIO",
      "references": [
        "other_io"
      ]
    },
    "references.io_references:test_io": {
      "id": "references.io_references:test_io",
      "name": "test_io",
      "type": "references.io_references:MyIO",
      "references": [
        "other_io"
      ]
    },
    "references.io_references:world": {
      "id": "references.io_references:world",
      "name": "world",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/io_references.py:1: error: Skipping analyzing "references": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/io_references.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```