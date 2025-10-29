## Resource

```python
from ordeq_manifest import create_manifest_json
from project import nodes_import_reassign

print(create_manifest_json(nodes_import_reassign))

```

## Output

```text
{
  "name": "project.nodes_import_reassign",
  "nodes": {
    "project.nodes_import_reassign:func_a": {
      "id": "project.nodes_import_reassign:func_a",
      "name": "func_a",
      "inputs": [
        "project.nodes_import_reassign:A|AA|a",
        "project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "project.nodes_import_reassign:f"
      ],
      "attributes": {}
    },
    "project.nodes_import_reassign:func_b": {
      "id": "project.nodes_import_reassign:func_b",
      "name": "func_b",
      "inputs": [
        "project.nodes_import_reassign:A|AA|a",
        "project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "project.nodes_import_reassign:f"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "project.nodes_import_reassign:A": {
      "id": "project.nodes_import_reassign:A",
      "name": "A",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_import_reassign:AA": {
      "id": "project.nodes_import_reassign:AA",
      "name": "AA",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_import_reassign:B": {
      "id": "project.nodes_import_reassign:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.nodes_import_reassign:BB": {
      "id": "project.nodes_import_reassign:BB",
      "name": "BB",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.nodes_import_reassign:a": {
      "id": "project.nodes_import_reassign:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_import_reassign:b": {
      "id": "project.nodes_import_reassign:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.nodes_import_reassign:f": {
      "id": "project.nodes_import_reassign:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_import_reassign.py:2: error: Skipping analyzing "project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_import_reassign.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```