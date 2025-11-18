## Resource

```python
import example_resources
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_resources))

```

## Output

```text
{
  "name": "example_resources",
  "nodes": {
    "example_resources.inline:generate": {
      "name": "generate",
      "inputs": [],
      "outputs": [
        "example_resources.inline:<anonymous0>"
      ],
      "attributes": {}
    },
    "example_resources.inline:consume": {
      "name": "consume",
      "inputs": [
        "example_resources.inline:<anonymous1>"
      ],
      "outputs": [
        "example_resources.inline:<anonymous2>"
      ],
      "attributes": {}
    },
    "example_resources.pipeline:generate": {
      "name": "generate",
      "inputs": [],
      "outputs": [
        "example_resources.pipeline:csv"
      ],
      "attributes": {}
    },
    "example_resources.pipeline:consume": {
      "name": "consume",
      "inputs": [
        "example_resources.pipeline:text"
      ],
      "outputs": [
        "example_resources.pipeline:<anonymous3>"
      ],
      "attributes": {}
    },
    "example_resources.updates:update": {
      "name": "update",
      "inputs": [
        "example_resources.updates:csv|csv_old|csv_new"
      ],
      "outputs": [
        "example_resources.updates:csv|csv_old|csv_new"
      ],
      "attributes": {}
    },
    "example_resources.updates:reflect": {
      "name": "reflect",
      "inputs": [
        "example_resources.updates:csv|csv_old|csv_new"
      ],
      "outputs": [
        "example_resources.updates:<anonymous4>"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_resources.pipeline:csv": {
      "name": "csv",
      "type": "ordeq_files.csv:CSV",
      "resource": 0,
      "references": [],
      "attributes": {}
    },
    "example_resources.pipeline:text": {
      "name": "text",
      "type": "ordeq_files.text:Text",
      "resource": 0,
      "references": [],
      "attributes": {}
    },
    "example_resources.updates:csv": {
      "name": "csv",
      "type": "ordeq_files.csv:CSV",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_resources.updates:csv_old": {
      "name": "csv_old",
      "type": "ordeq_files.csv:CSV",
      "resource": 1,
      "references": [],
      "attributes": {}
    },
    "example_resources.updates:csv_new": {
      "name": "csv_new",
      "type": "ordeq_files.csv:CSV",
      "resource": 2,
      "references": [],
      "attributes": {}
    },
    "example_resources.inline:<anonymous0>": {
      "name": "<anonymous0>",
      "type": "ordeq_files.csv:CSV",
      "resource": 3,
      "references": [],
      "attributes": {}
    },
    "example_resources.inline:<anonymous1>": {
      "name": "<anonymous1>",
      "type": "ordeq_files.text:Text",
      "resource": 3,
      "references": [],
      "attributes": {}
    },
    "example_resources.inline:<anonymous2>": {
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_resources.pipeline:<anonymous3>": {
      "name": "<anonymous3>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_resources.updates:<anonymous4>": {
      "name": "<anonymous4>",
      "type": "ordeq_common.io.printer:Print",
      "resource": null,
      "references": [],
      "attributes": {}
    }
  },
  "resources": [
    {
      "id": 0,
      "type": "pathlib._local:Path",
      "value": "data2.csv"
    },
    {
      "id": 1,
      "type": "builtins:str",
      "value": "old"
    },
    {
      "id": 2,
      "type": "builtins:str",
      "value": "new"
    },
    {
      "id": 3,
      "type": "pathlib._local:Path",
      "value": "data1.csv"
    }
  ]
}

```

## Logging

```text
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_resources.inline:consume'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_resources.pipeline:consume'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.

```