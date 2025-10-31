## Resource

```python
import example_project
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_project))

```

## Output

```text
{
  "name": "example_project",
  "nodes": {
    "example_project.inner.nodes:func": {
      "id": "example_project.inner.nodes:func",
      "name": "func",
      "inputs": [
        "example_project.inner.nodes:x"
      ],
      "outputs": [
        "example_project.inner.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "example_project.nodes:func": {
      "id": "example_project.nodes:func",
      "name": "func",
      "inputs": [
        "example_project.nodes:x"
      ],
      "outputs": [
        "example_project.nodes:y"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "example_project.nodes_import:func_a": {
      "id": "example_project.nodes_import:func_a",
      "name": "func_a",
      "inputs": [
        "example_project.nodes_import:a",
        "example_project.nodes_import:b"
      ],
      "outputs": [
        "example_project.nodes_import:f"
      ],
      "attributes": {}
    },
    "example_project.nodes_import:func_b": {
      "id": "example_project.nodes_import:func_b",
      "name": "func_b",
      "inputs": [
        "example_project.nodes_import:a",
        "example_project.nodes_import:b"
      ],
      "outputs": [
        "example_project.nodes_import:f"
      ],
      "attributes": {
        "tags": {
          "viz": "orange"
        }
      }
    },
    "example_project.nodes_import_alias:func": {
      "id": "example_project.nodes_import_alias:func",
      "name": "func",
      "inputs": [
        "example_project.nodes_import_alias:a",
        "example_project.nodes_import_alias:B"
      ],
      "outputs": [
        "example_project.nodes_import_alias:f"
      ],
      "attributes": {
        "tags": {
          "key": "threshold",
          "value": 0.23
        }
      }
    },
    "example_project.nodes_import_reassign:func_a": {
      "id": "example_project.nodes_import_reassign:func_a",
      "name": "func_a",
      "inputs": [
        "example_project.nodes_import_reassign:A|AA|a",
        "example_project.nodes_import_reassign:B|BB|b"
      ],
      "outputs": [
        "example_project.nodes_import_reassign:f"
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
        "example_project.nodes_import_reassign:f"
      ],
      "attributes": {}
    },
    "example_project.nodes_with_inline_io:greet": {
      "id": "example_project.nodes_with_inline_io:greet",
      "name": "greet",
      "inputs": [
        "example_project.nodes_with_inline_io:<anonymous0>"
      ],
      "outputs": [
        "example_project.nodes_with_inline_io:<anonymous1>"
      ],
      "attributes": {}
    },
    "example_project.nodes_with_view:farewell": {
      "id": "example_project.nodes_with_view:farewell",
      "name": "farewell",
      "inputs": [
        "example_project.nodes_with_view:greeting"
      ],
      "outputs": [
        "example_project.nodes_with_view:printer"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_project.catalog_1:a": {
      "id": "example_project.catalog_1:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.catalog_1:b": {
      "id": "example_project.catalog_1:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.catalog_1:c": {
      "id": "example_project.catalog_1:c",
      "name": "c",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.catalog_2:d": {
      "id": "example_project.catalog_2:d",
      "name": "d",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.catalog_2:e": {
      "id": "example_project.catalog_2:e",
      "name": "e",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.catalog_2:f": {
      "id": "example_project.catalog_2:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.inner.nodes:x": {
      "id": "example_project.inner.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.inner.nodes:y": {
      "id": "example_project.inner.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.nodes:x": {
      "id": "example_project.nodes:x",
      "name": "x",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes:y": {
      "id": "example_project.nodes:y",
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.nodes_import:a": {
      "id": "example_project.nodes_import:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_import:b": {
      "id": "example_project.nodes_import:b",
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.nodes_import:f": {
      "id": "example_project.nodes_import:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.nodes_import_alias:B": {
      "id": "example_project.nodes_import_alias:B",
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": []
    },
    "example_project.nodes_import_alias:a": {
      "id": "example_project.nodes_import_alias:a",
      "name": "a",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_import_alias:f": {
      "id": "example_project.nodes_import_alias:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
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
    "example_project.nodes_import_reassign:f": {
      "id": "example_project.nodes_import_reassign:f",
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    },
    "example_project.nodes_with_inline_io:<anonymous0>": {
      "id": "example_project.nodes_with_inline_io:<anonymous0>",
      "name": "<anonymous0>",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_with_inline_io:<anonymous1>": {
      "id": "example_project.nodes_with_inline_io:<anonymous1>",
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes_with_view:<anonymous2>": {
      "id": "example_project.nodes_with_view:<anonymous2>",
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "references": []
    },
    "example_project.nodes_with_view:greeting": {
      "id": "example_project.nodes_with_view:greeting",
      "name": "greeting",
      "type": "ordeq_common.io.literal:Literal",
      "references": []
    },
    "example_project.nodes_with_view:printer": {
      "id": "example_project.nodes_with_view:printer",
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "references": []
    }
  }
}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```