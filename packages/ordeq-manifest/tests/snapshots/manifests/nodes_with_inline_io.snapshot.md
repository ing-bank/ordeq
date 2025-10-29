## Resource

```python
from ordeq_manifest import create_manifest_json
from project import nodes_with_inline_io

print(create_manifest_json(nodes_with_inline_io))

```

## Output

```text
{
  "name": "project.nodes_with_inline_io",
  "nodes": {
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
    }
  },
  "ios": {
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
    }
  }
}

```

## Typing

```text
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: error: Skipping analyzing "project": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-manifest/tests/resources/manifests/nodes_with_inline_io.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```