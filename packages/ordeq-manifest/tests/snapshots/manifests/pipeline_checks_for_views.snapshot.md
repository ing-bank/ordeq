## Resource

```python
import example_checks.pipeline_checks_for_views
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_checks.pipeline_checks_for_views))

```

## Output

```text
{
  "name": "example_checks.pipeline_checks_for_views",
  "nodes": {
    "example_checks.pipeline_checks_for_views:Ap": {
      "name": "Ap",
      "inputs": [
        "example_checks.pipeline_checks_for_views:A"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous0>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:Bp": {
      "name": "Bp",
      "inputs": [
        "example_checks.pipeline_checks_for_views:B"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:AB": {
      "name": "AB",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous0>",
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous2>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:print_result": {
      "name": "print_result",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous2>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous3>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:check_a": {
      "name": "check_a",
      "inputs": [
        "example_checks.pipeline_checks_for_views:A",
        "example_checks.pipeline_checks_for_views:D"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous4>"
      ],
      "checks": [
        "example_checks.pipeline_checks_for_views:A"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:check_ap": {
      "name": "check_ap",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous0>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous5>"
      ],
      "checks": [
        "example_checks.pipeline_checks_for_views:<anonymous0>"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:check_bp": {
      "name": "check_bp",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous6>"
      ],
      "checks": [
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:check_join": {
      "name": "check_join",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous0>",
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous7>"
      ],
      "checks": [
        "example_checks.pipeline_checks_for_views:<anonymous0>",
        "example_checks.pipeline_checks_for_views:<anonymous1>"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:check_ab": {
      "name": "check_ab",
      "inputs": [
        "example_checks.pipeline_checks_for_views:<anonymous2>"
      ],
      "outputs": [
        "example_checks.pipeline_checks_for_views:<anonymous8>"
      ],
      "checks": [
        "example_checks.pipeline_checks_for_views:<anonymous2>"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_checks.pipeline_checks_for_views:A": {
      "name": "A",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:B": {
      "name": "B",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:D": {
      "name": "D",
      "type": "ordeq._io:Input",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous0>": {
      "name": "<anonymous0>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous1>": {
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous2>": {
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous3>": {
      "name": "<anonymous3>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous4>": {
      "name": "<anonymous4>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous5>": {
      "name": "<anonymous5>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous6>": {
      "name": "<anonymous6>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous7>": {
      "name": "<anonymous7>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_for_views:<anonymous8>": {
      "name": "<anonymous8>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    }
  },
  "resources": []
}

```

## Logging

```text
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.

```