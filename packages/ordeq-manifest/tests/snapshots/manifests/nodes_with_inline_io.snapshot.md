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
  "modules": [],
  "nodes": {
    "example_project.nodes_with_inline_io:greet": {
      "inputs": [
        "io-0"
      ],
      "outputs": [
        "io-1"
      ],
      "attributes": {},
      "view": false
    }
  },
  "ios": {
    "io-0": {
      "type": "ordeq_common.io.literal:Literal",
      "references": {}
    },
    "io-1": {
      "type": "ordeq._io:IO",
      "references": {}
    }
  }
}

```