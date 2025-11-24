## Resource

```python
import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._static import _module_to_imports

submodules = list(_resolve_packages_to_modules(example_rag_pipeline))
for submodule in submodules:
    print(submodule.__name__, _module_to_imports(submodule))

```

## Output

```text
example_rag_pipeline {}
example_rag_pipeline.catalog {'Any': 'typing', 'IO': 'ordeq'}
example_rag_pipeline.rag {}
example_rag_pipeline.rag.annotation {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}
example_rag_pipeline.rag.evaluation {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}
example_rag_pipeline.rag.indexer {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}
example_rag_pipeline.rag.policies {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}
example_rag_pipeline.rag.question_answering {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}
example_rag_pipeline.rag.retrieval {'node': 'ordeq', 'catalog': 'example_rag_pipeline'}

```