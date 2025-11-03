## Resource

```python
import example_references
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_references))

```

## Output

```text
{
  "name": "example_references",
  "modules": [
    {
      "name": "example_references.io_references",
      "nodes": {},
      "ios": {
        "test_io": "io-7",
        "nested_test_io": "io-4",
        "world": "io-2",
        "named_test_io": "io-3",
        "named_nested_test_io": "io-0"
      }
    }
  ],
  "nodes": {},
  "ios": {
    "io-0": {
      "name": "named_nested_test_io",
      "type": "example_references.io_references:MyIO",
      "references": {
        "other_io": [
          "io-1"
        ]
      }
    },
    "io-2": {
      "name": "world",
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-3": {
      "name": "named_test_io",
      "type": "example_references.io_references:MyIO",
      "references": {
        "other_io": [
          "io-2"
        ]
      }
    },
    "io-4": {
      "name": "nested_test_io",
      "type": "example_references.io_references:MyIO",
      "references": {
        "other_io": [
          "io-5"
        ]
      }
    },
    "io-7": {
      "name": "test_io",
      "type": "example_references.io_references:MyIO",
      "references": {
        "other_io": [
          "io-8"
        ]
      }
    }
  }
}

```