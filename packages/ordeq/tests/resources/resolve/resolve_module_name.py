import example_rag_pipeline
from ordeq._resolve import _resolve_module_name_to_module

print("Should print 'example_rag_pipeline':")
print(_resolve_module_name_to_module("example_rag_pipeline").__name__)

print("Should print 'example_rag_pipeline':")
print(_resolve_module_name_to_module(example_rag_pipeline).__name__)

print("Should raise an error:")
_ = _resolve_module_name_to_module(0.123)
