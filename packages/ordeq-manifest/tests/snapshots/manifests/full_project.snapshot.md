## Resource

```python
from ordeq_manifest import create_manifest_json
import project

print(create_manifest_json(project))

```

## Output

```text
{
  "name": "project",
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
    },
    "project.nodes:func": {
      "id": "project.nodes:func",
      "name": "func",
      "inputs": [
        "project.nodes:x"
      ],
      "outputs": [
        "project.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "project.nodes_import:func_a": {
      "id": "project.nodes_import:func_a",
      "name": "func_a",
      "inputs": [
        "project.nodes_import:a",
        "project.nodes_import:b"
      ],
      "outputs": [
        "project.nodes_import:f"
      ],
      "attributes": {}
    },
    "project.nodes_import:func_b": {
      "id": "project.nodes_import:func_b",
      "name": "func_b",
      "inputs": [
        "project.nodes_import:a",
        "project.nodes_import:b"
      ],
      "outputs": [
        "project.nodes_import:f"
      ],
      "attributes": {
        "tags": {
          "viz": "orange"
        }
      }
    },
    "project.nodes_import_alias:func": {
      "id": "project.nodes_import_alias:func",
      "name": "func",
      "inputs": [
        "project.nodes_import_alias:a",
        "project.nodes_import_alias:B"
      ],
      "outputs": [
        "project.nodes_import_alias:f"
      ],
      "attributes": {
        "tags": {
          "key": "threshold",
          "value": 0.23
        }
      }
    },
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
    },
    "project.nodes_with_inline_io:greet": {
      "id": "project.nodes_with_inline_io:greet",
      "name": "greet",
      "inputs": [
        "project.nodes_with_inline_io:<anonymous0>"
      ],
      "outputs": [
        "project.nodes_with_inline_io:<anonymous1>"
      ],
      "attributes": {}
    },
    "project.nodes_with_view:farewell": {
      "id": "project.nodes_with_view:farewell",
      "name": "farewell",
      "inputs": [
        "project.nodes_with_view:greeting"
      ],
      "outputs": [
        "project.nodes_with_view:printer"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "project.catalog_1:a": {
      "id": "project.catalog_1:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.catalog_1:b": {
      "id": "project.catalog_1:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.catalog_1:c": {
      "id": "project.catalog_1:c",
      "name": "c",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "project.catalog_2:d": {
      "id": "project.catalog_2:d",
      "name": "d",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.catalog_2:e": {
      "id": "project.catalog_2:e",
      "name": "e",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.catalog_2:f": {
      "id": "project.catalog_2:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
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
    },
    "project.nodes:x": {
      "id": "project.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "project.nodes:y": {
      "id": "project.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "project.nodes_import:a": {
      "id": "project.nodes_import:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_import:b": {
      "id": "project.nodes_import:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.nodes_import:f": {
      "id": "project.nodes_import:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "project.nodes_import_alias:B": {
      "id": "project.nodes_import_alias:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "project.nodes_import_alias:a": {
      "id": "project.nodes_import_alias:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_import_alias:f": {
      "id": "project.nodes_import_alias:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
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
    },
    "project.nodes_with_inline_io:<anonymous0>": {
      "id": "project.nodes_with_inline_io:<anonymous0>",
      "name": "<anonymous0>",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_with_inline_io:<anonymous1>": {
      "id": "project.nodes_with_inline_io:<anonymous1>",
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "project.nodes_with_view:<anonymous2>": {
      "id": "project.nodes_with_view:<anonymous2>",
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "project.nodes_with_view:greeting": {
      "id": "project.nodes_with_view:greeting",
      "name": "greeting",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "project.nodes_with_view:printer": {
      "id": "project.nodes_with_view:printer",
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/full_project.py:2: error: Skipping analyzing "project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/full_project.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```