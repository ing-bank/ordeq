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
      "name": "func",
      "inputs": [
        "example_project.inner.nodes:x"
      ],
      "outputs": [
        "example_project.inner.nodes:y"
      ],
      "checks": [],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "example_project.nodes:func": {
      "name": "func",
      "inputs": [
        "example_project.nodes:x"
      ],
      "outputs": [
        "example_project.nodes:y"
      ],
      "checks": [],
      "attributes": {
        "tags": [
          "dummy"
        ]
      }
    },
    "example_project.nodes_import:func_a": {
      "name": "func_a",
      "inputs": [
        "example_project.nodes_import:a",
        "example_project.nodes_import:b"
      ],
      "outputs": [
        "example_project.nodes_import:f"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_project.nodes_import:func_b": {
      "name": "func_b",
      "inputs": [
        "example_project.nodes_import:a",
        "example_project.nodes_import:b"
      ],
      "outputs": [
        "example_project.catalog_2:g"
      ],
      "checks": [],
      "attributes": {
        "tags": {
          "viz": "orange"
        }
      }
    },
    "example_project.nodes_import_alias:func": {
      "name": "func",
      "inputs": [
        "example_project.nodes_import_alias:a",
        "example_project.nodes_import_alias:B"
      ],
      "outputs": [
        "example_project.nodes_import_alias:h"
      ],
      "checks": [],
      "attributes": {
        "tags": {
          "key": "threshold",
          "value": 0.23
        }
      }
    },
    "example_project.nodes_with_inline_io:greet": {
      "name": "greet",
      "inputs": [
        "example_project.nodes_with_inline_io:<anonymous0>"
      ],
      "outputs": [
        "example_project.nodes_with_inline_io:<anonymous1>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_project.nodes_with_view:greet": {
      "name": "greet",
      "inputs": [
        "example_project.nodes_with_view:greeting"
      ],
      "outputs": [
        "example_project.nodes_with_view:<anonymous2>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_project.nodes_with_view:farewell": {
      "name": "farewell",
      "inputs": [
        "example_project.nodes_with_view:<anonymous2>"
      ],
      "outputs": [
        "example_project.nodes_with_view:printer"
      ],
      "checks": [],
      "attributes": {}
    }
  },
  "ios": {
    "example_project.catalog_1:a": {
      "name": "a",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_1:b": {
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_1:c": {
      "name": "c",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:d": {
      "name": "d",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:e": {
      "name": "e",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:f": {
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:g": {
      "name": "g",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:h": {
      "name": "h",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:i": {
      "name": "i",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.catalog_2:j": {
      "name": "j",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.inner.nodes:x": {
      "name": "x",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.inner.nodes:y": {
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes:x": {
      "name": "x",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes:y": {
      "name": "y",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import:a": {
      "name": "a",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import:b": {
      "name": "b",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import:f": {
      "name": "f",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import_alias:a": {
      "name": "a",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import_alias:B": {
      "name": "B",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_import_alias:h": {
      "name": "h",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_view:greeting": {
      "name": "greeting",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_view:printer": {
      "name": "printer",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_inline_io:<anonymous0>": {
      "name": "<anonymous0>",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_inline_io:<anonymous1>": {
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_view:<anonymous2>": {
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    }
  },
  "resources": []
}

```