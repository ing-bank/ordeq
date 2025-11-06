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
  "nodes": {
    "example_project.nodes_import_reassign:func_a": {
      "id": "example_project.nodes_import_reassign:func_a",
      "name": "func_a",
      "inputs": [
        "example_project.nodes_import_reassign:A|AA|a",
        "example_project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "example_project.nodes_import_reassign:i"
      ],
      "attributes": {}
    },
    "example_project.nodes_import_reassign:func_b": {
      "id": "example_project.nodes_import_reassign:func_b",
      "name": "func_b",
      "inputs": [
        "example_project.nodes_import_reassign:A|AA|a",
        "example_project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "example_project.nodes_import_reassign:j"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_project.nodes_import_reassign:A": {
      "id": "example_project.nodes_import_reassign:A",
      "name": "A",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_import_reassign:AA": {
      "id": "example_project.nodes_import_reassign:AA",
      "name": "AA",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_import_reassign:B": {
      "id": "example_project.nodes_import_reassign:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.nodes_import_reassign:BB": {
      "id": "example_project.nodes_import_reassign:BB",
      "name": "BB",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.nodes_import_reassign:a": {
      "id": "example_project.nodes_import_reassign:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_import_reassign:b": {
      "id": "example_project.nodes_import_reassign:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.nodes_import_reassign:i": {
      "id": "example_project.nodes_import_reassign:i",
      "name": "i",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.nodes_import_reassign:j": {
      "id": "example_project.nodes_import_reassign:j",
      "name": "j",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```