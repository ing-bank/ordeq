## Resource

```python
import example_references
from ordeq_manifest import create_manifest_json

print(create_manifest_json(example_references))

```

## Exception

```text
ValidationError: 1 validation error for ProjectModel
  Value error, Referenced IO 'io-1' in IO 'type='example_references.io_references:MyIO' references={'other_io': ['io-1']}' not found in project IOs. [type=value_error, input_value={'name': 'example_referen...'other_io': ['io-8']})}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/value_error
  File "/.venv/lib/python3.13/site-packages/pydantic/main.py", line LINO, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)

  File "/packages/ordeq-manifest/src/ordeq_manifest/models.py", line LINO, in from_nodes_and_ios
    return cls(
        name=name,
    ...<2 lines>...
        ios=dict(_sort_dict_items(io_models)),
    )

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest
    return ProjectModel.from_nodes_and_ios(name=name, nodes=nodes, ios=ios)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq-manifest/src/ordeq_manifest/manifest.py", line LINO, in create_manifest_json
    project_model = create_manifest(package)

  File "/packages/ordeq-manifest/tests/resources/manifests/io_references.py", line LINO, in <module>
    print(create_manifest_json(example_references))
          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```