## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("examples.rag_pipeline.rag.annotation"),
    importlib.import_module("examples.rag_pipeline.rag.evaluation"),
    importlib.import_module("examples.rag_pipeline.rag.indexer"),
    importlib.import_module("examples.rag_pipeline.rag.policies"),
    importlib.import_module("examples.rag_pipeline.rag.question_answering"),
    importlib.import_module("examples.rag_pipeline.rag.retrieval"),
    importlib.import_module("examples.rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(list(ios.keys()))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['examples.rag_pipeline.rag.annotation', 'examples.rag_pipeline.rag.evaluation', 'examples.rag_pipeline.rag.indexer', 'examples.rag_pipeline.rag.policies', 'examples.rag_pipeline.rag.question_answering', 'examples.rag_pipeline.rag.retrieval', 'examples.rag_pipeline.catalog']
['examples.rag_pipeline.rag.annotation:annotate_documents', 'examples.rag_pipeline.rag.evaluation:evaluate_answers', 'examples.rag_pipeline.rag.indexer:create_vector_index', 'examples.rag_pipeline.rag.policies:generate_questions', 'examples.rag_pipeline.rag.question_answering:question_answering', 'examples.rag_pipeline.rag.retrieval:filter_relevant', 'examples.rag_pipeline.rag.retrieval:retrieve']
[('examples.rag_pipeline.catalog', 'policies'), ('examples.rag_pipeline.catalog', 'llm_model'), ('examples.rag_pipeline.catalog', 'llm_vision_retrieval_model'), ('examples.rag_pipeline.catalog', 'pdf_documents'), ('examples.rag_pipeline.catalog', 'retrieved_pages'), ('examples.rag_pipeline.catalog', 'relevant_pages'), ('examples.rag_pipeline.catalog', 'index'), ('examples.rag_pipeline.catalog', 'questions'), ('examples.rag_pipeline.catalog', 'metrics'), ('examples.rag_pipeline.catalog', 'pdfs_documents_annotated'), ('examples.rag_pipeline.catalog', 'llm_answers')]
['examples.rag_pipeline.rag.annotation:annotate_documents', 'examples.rag_pipeline.rag.evaluation:evaluate_answers', 'examples.rag_pipeline.rag.indexer:create_vector_index', 'examples.rag_pipeline.rag.policies:generate_questions', 'examples.rag_pipeline.rag.question_answering:question_answering', 'examples.rag_pipeline.rag.retrieval:filter_relevant', 'examples.rag_pipeline.rag.retrieval:retrieve']

```