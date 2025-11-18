## Resource

```python
from example_project import nodes_with_inline_io
from ordeq_manifest import create_manifest_json

print(create_manifest_json(nodes_with_inline_io))

```

## Output

```text
{
  "name": "example_project.nodes_with_inline_io",
  "nodes": {
    "example_project.nodes_with_inline_io:greet": {
      "name": "greet",
      "inputs": [
        "example_project.nodes_with_inline_io:<anonymous0>"
      ],
      "outputs": [
        "example_project.nodes_with_inline_io:<anonymous1>"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_project.nodes_with_inline_io:<anonymous0>": {
      "name": "<anonymous0>",
      "type": "ordeq_common.io.literal:Literal",
      "references": [],
      "attributes": {}
    },
    "example_project.nodes_with_inline_io:<anonymous1>": {
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "references": [],
      "attributes": {}
    }
  }
}

```