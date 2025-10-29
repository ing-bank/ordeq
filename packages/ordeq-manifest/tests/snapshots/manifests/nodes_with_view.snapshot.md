## Resource

```python
from ordeq_manifest import create_manifest_json
from examples.project import nodes_with_view

print(create_manifest_json(nodes_with_view))

```

## Output

```text
{
  "name": "examples.project.nodes_with_view",
  "nodes": {
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
    "examples.project.nodes_with_view:<anonymous0>": {
      "id": "examples.project.nodes_with_view:<anonymous0>",
      "name": "<anonymous0>",
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
packages/ordeq-manifest/tests/resources/manifests/nodes_with_view.py:2: error: Skipping analyzing "examples.project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_with_view.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```