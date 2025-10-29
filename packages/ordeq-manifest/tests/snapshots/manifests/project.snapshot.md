## Resource

```python
from ordeq_manifest import create_manifest_json
import examples.project

print(create_manifest_json(examples.project))

```

## Output

```text
{
  "name": "examples.project",
  "nodes": {
    "examples.project.inner.nodes:func": {
      "id": "examples.project.inner.nodes:func",
      "name": "func",
      "inputs": [
        "examples.project.inner.nodes:x"
      ],
      "outputs": [
        "examples.project.inner.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "examples.project.nodes:func": {
      "id": "examples.project.nodes:func",
      "name": "func",
      "inputs": [
        "examples.project.nodes:x"
      ],
      "outputs": [
        "examples.project.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "examples.project.nodes_import:func_a": {
      "id": "examples.project.nodes_import:func_a",
      "name": "func_a",
      "inputs": [
        "examples.project.nodes_import:a",
        "examples.project.nodes_import:b"
      ],
      "outputs": [
        "examples.project.nodes_import:f"
      ],
      "attributes": {}
    },
    "examples.project.nodes_import:func_b": {
      "id": "examples.project.nodes_import:func_b",
      "name": "func_b",
      "inputs": [
        "examples.project.nodes_import:a",
        "examples.project.nodes_import:b"
      ],
      "outputs": [
        "examples.project.nodes_import:f"
      ],
      "attributes": {
        "tags": {
          "viz": "orange"
        }
      }
    },
    "examples.project.nodes_import_alias:func": {
      "id": "examples.project.nodes_import_alias:func",
      "name": "func",
      "inputs": [
        "examples.project.nodes_import_alias:a",
        "examples.project.nodes_import_alias:B"
      ],
      "outputs": [
        "examples.project.nodes_import_alias:f"
      ],
      "attributes": {
        "tags": {
          "key": "threshold",
          "value": 0.23
        }
      }
    },
    "examples.project.nodes_import_reassign:func_a": {
      "id": "examples.project.nodes_import_reassign:func_a",
      "name": "func_a",
      "inputs": [
        "examples.project.nodes_import_reassign:A|AA|a",
        "examples.project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "examples.project.nodes_import_reassign:f"
      ],
      "attributes": {}
    },
    "examples.project.nodes_import_reassign:func_b": {
      "id": "examples.project.nodes_import_reassign:func_b",
      "name": "func_b",
      "inputs": [
        "examples.project.nodes_import_reassign:A|AA|a",
        "examples.project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "examples.project.nodes_import_reassign:f"
      ],
      "attributes": {}
    },
    "examples.project.nodes_with_inline_io:greet": {
      "id": "examples.project.nodes_with_inline_io:greet",
      "name": "greet",
      "inputs": [
        "examples.project.nodes_with_inline_io:<anonymous0>"
      ],
      "outputs": [
        "examples.project.nodes_with_inline_io:<anonymous1>"
      ],
      "attributes": {}
    },
    "examples.project.nodes_with_view:farewell": {
      "id": "examples.project.nodes_with_view:farewell",
      "name": "farewell",
      "inputs": [
        "examples.project.nodes_with_view:greeting"
      ],
      "outputs": [
        "examples.project.nodes_with_view:printer"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "examples.project.catalog_1:a": {
      "id": "examples.project.catalog_1:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.catalog_1:b": {
      "id": "examples.project.catalog_1:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.catalog_1:c": {
      "id": "examples.project.catalog_1:c",
      "name": "c",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.catalog_2:d": {
      "id": "examples.project.catalog_2:d",
      "name": "d",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.catalog_2:e": {
      "id": "examples.project.catalog_2:e",
      "name": "e",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.catalog_2:f": {
      "id": "examples.project.catalog_2:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.inner.nodes:x": {
      "id": "examples.project.inner.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "examples.project.inner.nodes:y": {
      "id": "examples.project.inner.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.nodes:x": {
      "id": "examples.project.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "examples.project.nodes:y": {
      "id": "examples.project.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.nodes_import:a": {
      "id": "examples.project.nodes_import:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_import:b": {
      "id": "examples.project.nodes_import:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.nodes_import:f": {
      "id": "examples.project.nodes_import:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.nodes_import_alias:B": {
      "id": "examples.project.nodes_import_alias:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_alias:a": {
      "id": "examples.project.nodes_import_alias:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_import_alias:f": {
      "id": "examples.project.nodes_import_alias:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.nodes_import_reassign:A": {
      "id": "examples.project.nodes_import_reassign:A",
      "name": "A",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign:AA": {
      "id": "examples.project.nodes_import_reassign:AA",
      "name": "AA",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign:B": {
      "id": "examples.project.nodes_import_reassign:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign:BB": {
      "id": "examples.project.nodes_import_reassign:BB",
      "name": "BB",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign:a": {
      "id": "examples.project.nodes_import_reassign:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_import_reassign:b": {
      "id": "examples.project.nodes_import_reassign:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "examples.project.nodes_import_reassign:f": {
      "id": "examples.project.nodes_import_reassign:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "examples.project.nodes_with_inline_io:<anonymous0>": {
      "id": "examples.project.nodes_with_inline_io:<anonymous0>",
      "name": "<anonymous0>",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_with_inline_io:<anonymous1>": {
      "id": "examples.project.nodes_with_inline_io:<anonymous1>",
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "examples.project.nodes_with_view:<anonymous2>": {
      "id": "examples.project.nodes_with_view:<anonymous2>",
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "examples.project.nodes_with_view:greeting": {
      "id": "examples.project.nodes_with_view:greeting",
      "name": "greeting",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "examples.project.nodes_with_view:printer": {
      "id": "examples.project.nodes_with_view:printer",
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'examples.project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/project.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/project.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```