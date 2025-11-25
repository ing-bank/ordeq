## Resource

```python
from ordeq._resolve import _resolve_module_name_to_module
import example_rag_pipeline

print("Should print 'example_rag_pipeline':")
print(_resolve_module_name_to_module("example_rag_pipeline").__name__)

print("Should print 'example_rag_pipeline':")
print(_resolve_module_name_to_module(example_rag_pipeline).__name__)

print("Should raise an error:")
_ = _resolve_module_name_to_module(0.123)

```

## Output

```text
Should print 'example_rag_pipeline':
example_rag_pipeline
Should print 'example_rag_pipeline':
example_rag_pipeline
Should raise an error:
TypeError: '0.123' is not a valid module. Expected a ModuleType or a string, got float
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_name_to_module
    raise TypeError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/resolve/resolve_module_name.py", line LINO, in <module>
    _ = _resolve_module_name_to_module(0.123)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```