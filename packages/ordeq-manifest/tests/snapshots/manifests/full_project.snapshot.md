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
  "modules": [
    {
      "name": "example_project.catalog_1",
      "nodes": {},
      "ios": {
        "a": "io-0",
        "b": "io-1",
        "c": "io-2"
      }
    },
    {
      "name": "example_project.catalog_2",
      "nodes": {},
      "ios": {
        "d": "io-3",
        "e": "io-4",
        "f": "io-5"
      }
    },
    {
      "name": "example_project.inner.nodes",
      "nodes": {
        "func": "example_project.inner.nodes:func"
      },
      "ios": {
        "x": "io-6",
        "y": "io-7"
      }
    },
    {
      "name": "example_project.nodes",
      "nodes": {
        "func": "example_project.nodes:func"
      },
      "ios": {
        "x": "io-8",
        "y": "io-9"
      }
    },
    {
      "name": "example_project.nodes_import",
      "nodes": {
        "func_a": "example_project.nodes_import:func_a",
        "func_b": "example_project.nodes_import:func_b"
      },
      "ios": {
        "a": "io-0",
        "b": "io-1",
        "f": "io-5"
      }
    },
    {
      "name": "example_project.nodes_import_alias",
      "nodes": {
        "func": "example_project.nodes_import_alias:func"
      },
      "ios": {
        "a": "io-0",
        "B": "io-1",
        "f": "io-5"
      }
    },
    {
      "name": "example_project.nodes_import_reassign",
      "nodes": {
        "func_a": "example_project.nodes_import_reassign:func_a",
        "func_b": "example_project.nodes_import_reassign:func_b"
      },
      "ios": {
        "a": "io-0",
        "b": "io-1",
        "f": "io-5",
        "A": "io-0",
        "B": "io-1",
        "AA": "io-0",
        "BB": "io-1"
      }
    },
    {
      "name": "example_project.nodes_with_view",
      "nodes": {
        "farewell": "example_project.nodes_with_view:farewell",
        "greet": "example_project.nodes_with_view:greet"
      },
      "ios": {
        "printer": "io-10",
        "<anonymous2>": "io-13",
        "<anonymous3>": "io-14"
      }
    }
  ],
  "nodes": {
    "example_project.inner.nodes:func": {
      "inputs": [
        "io-6"
      ],
      "outputs": [
        "io-7"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      },
      "view": false
    },
    "example_project.nodes:func": {
      "inputs": [
        "io-8"
      ],
      "outputs": [
        "io-9"
      ],
      "attributes": {
        "tags": [
          "dummy"
        ]
      },
      "view": false
    },
    "example_project.nodes_import:func_a": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-5"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_import:func_b": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-5"
      ],
      "attributes": {
        "tags": {
          "viz": "orange"
        }
      },
      "view": false
    },
    "example_project.nodes_import_alias:func": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-5"
      ],
      "attributes": {
        "tags": {
          "key": "threshold",
          "value": 0.23
        }
      },
      "view": false
    },
    "example_project.nodes_import_reassign:func_a": {
      "inputs": [
        "io-0",
        "io-1"
      ],
      "outputs": [
        "io-5"
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
        "io-5"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_with_inline_io:greet": {
      "inputs": [
        "io-11"
      ],
      "outputs": [
        "io-12"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_with_view:farewell": {
      "inputs": [
        "example_project.nodes_with_view:greet"
      ],
      "outputs": [
        "io-10"
      ],
      "attributes": {},
      "view": false
    },
    "example_project.nodes_with_view:greet": {
      "inputs": [],
      "outputs": [
        "io-14"
      ],
      "attributes": {},
      "view": true
    }
  },
  "ios": {
    "io-0": {
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-1": {
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": {}
    },
    "io-10": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    },
    "io-11": {
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-12": {
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-13": {
      "type": "ordeq._nodes:View",
      "references": {}
    },
    "io-14": {
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-2": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    },
    "io-3": {
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-4": {
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "references": {}
    },
    "io-5": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    },
    "io-6": {
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-7": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    },
    "io-8": {
      "type": "ordeq._io:IO",
      "references": {}
    },
    "io-9": {
      "type": "ordeq_common.io.printer:Print",
      "references": {}
    }
  }
}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```