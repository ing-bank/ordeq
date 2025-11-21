## Resource

```python
import example_checks.pipeline_checks_as_checks
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_checks.pipeline_checks_as_checks))

```

## Output

```text
{
  "name": "example_checks.pipeline_checks_as_checks",
  "nodes": {
    "example_checks.pipeline_checks_as_checks:process_a": {
      "name": "process_a",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:A"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:Ap"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:process_b": {
      "name": "process_b",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:B"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:join": {
      "name": "join",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:Ap",
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:AB"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:print_result": {
      "name": "print_result",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:AB"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous0>"
      ],
      "checks": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:check_a": {
      "name": "check_a",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:A",
        "example_checks.pipeline_checks_as_checks:D"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous1>"
      ],
      "checks": [
        "example_checks.pipeline_checks_as_checks:A"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:check_ap": {
      "name": "check_ap",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:Ap"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous2>"
      ],
      "checks": [
        "example_checks.pipeline_checks_as_checks:Ap"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:check_bp": {
      "name": "check_bp",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous3>"
      ],
      "checks": [
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:check_join": {
      "name": "check_join",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:Ap",
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous4>"
      ],
      "checks": [
        "example_checks.pipeline_checks_as_checks:Ap",
        "example_checks.pipeline_checks_as_checks:Bp"
      ],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:check_ab": {
      "name": "check_ab",
      "inputs": [
        "example_checks.pipeline_checks_as_checks:AB"
      ],
      "outputs": [
        "example_checks.pipeline_checks_as_checks:<anonymous5>"
      ],
      "checks": [
        "example_checks.pipeline_checks_as_checks:AB"
      ],
      "attributes": {}
    }
  },
  "ios": {
    "example_checks.pipeline_checks_as_checks:A": {
      "name": "A",
      "type": "ordeq_common.io.literal:Literal",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:B": {
      "name": "B",
      "type": "ordeq_common.io.literal:Literal",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:Ap": {
      "name": "Ap",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:Bp": {
      "name": "Bp",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:AB": {
      "name": "AB",
      "type": "ordeq_common.io.string_buffer:StringBuffer",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:D": {
      "name": "D",
      "type": "ordeq_common.io.literal:Literal",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous0>": {
      "name": "<anonymous0>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous1>": {
      "name": "<anonymous1>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous2>": {
      "name": "<anonymous2>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous3>": {
      "name": "<anonymous3>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous4>": {
      "name": "<anonymous4>",
      "type": "ordeq._io:IO",
      "resource": null,
      "references": [],
      "attributes": {}
    },
    "example_checks.pipeline_checks_as_checks:<anonymous5>": {
      "name": "<anonymous5>",
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