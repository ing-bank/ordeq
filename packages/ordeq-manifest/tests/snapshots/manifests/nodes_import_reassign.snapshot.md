## Resource

```python
from example_project import nodes_import_reassign
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes_import_reassign))

```

## Output

```text
{
  "name": "example_project.nodes_import_reassign",
  "modules": [
    {
      "name": "example_project.nodes_import_reassign",
      "nodes": {
        "func_a": "example_project.nodes_import_reassign:func_a",
        "func_b": "example_project.nodes_import_reassign:func_b"
      },
      "ios": {
        "a": "io-0",
        "b": "io-1",
        "f": "io-2",
        "A": "io-0",
        "B": "io-1",
        "AA": "io-0",
        "BB": "io-1"
      }
    }
  ],
  "nodes": {
    "example_project.nodes_import_reassign:func_a": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-2"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_import_reassign:func_b": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-2"
      ],
      "attributes": {},
      "view": false
    }
  },
  "ios": {
    "io-0": {
      "name": "AA",
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-1": {
      "name": "BB",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": {}
    },
    "io-2": {
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    }
  }
}

```