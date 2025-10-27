## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import nodes_import_reassign

print(create_manifest_json(nodes_import_reassign))

```

## Output

```text
{
  "name": "examples.project.nodes_import_reassign",
  "nodes": {
    "nodes.examples.project.nodes_import_reassign:func_a": {
      "id": "nodes.examples.project.nodes_import_reassign:func_a",
      "name": "examples.project.nodes_import_reassign:func_a",
      "inputs": [
        "examples.project.nodes_import_reassign.AA",
        "examples.project.nodes_import_reassign.BB"
      ],
      "outputs": [
        "examples.project.nodes_import_reassign.f"
      ],
      "attributes": {}
    },
    "nodes.examples.project.nodes_import_reassign:func_b": {
      "id": "nodes.examples.project.nodes_import_reassign:func_b",
      "name": "examples.project.nodes_import_reassign:func_b",
      "inputs": [
        "examples.project.nodes_import_reassign.AA",
        "examples.project.nodes_import_reassign.BB"
      ],
      "outputs": [
        "examples.project.nodes_import_reassign.f"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "examples.project.nodes_import_reassign.A": {
      "id": "examples.project.nodes_import_reassign.A",
      "name": "A",
      "type": "ordeq_common.io.literal.Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign.AA": {
      "id": "examples.project.nodes_import_reassign.AA",
      "name": "AA",
      "type": "ordeq_common.io.literal.Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign.B": {
      "id": "examples.project.nodes_import_reassign.B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer.StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign.BB": {
      "id": "examples.project.nodes_import_reassign.BB",
      "name": "BB",
      "type": "ordeq_common.io.string_buffer.StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign.a": {
      "id": "examples.project.nodes_import_reassign.a",
      "name": "a",
      "type": "ordeq_common.io.literal.Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign.b": {
      "id": "examples.project.nodes_import_reassign.b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer.StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign.f": {
      "id": "examples.project.nodes_import_reassign.f",
      "name": "f",
      "type": "ordeq_common.io.printer.Print",
      "references": []
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_import_reassign.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_import_reassign.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```