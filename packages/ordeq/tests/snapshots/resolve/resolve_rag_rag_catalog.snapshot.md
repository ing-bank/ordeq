## Resource

```python
import importlib

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_rag_pipeline.rag"),
    importlib.import_module("example_rag_pipeline.catalog"),
]

modules = list(dict(_resolve_runnables_to_modules(*runnables)).keys())
print(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
print(sorted(node.name for node in nodes))
print(dict(sorted(ios.items())))

print(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_rag_pipeline.rag', 'example_rag_pipeline.rag.annotation', 'example_rag_pipeline.rag.evaluation', 'example_rag_pipeline.rag.indexer', 'example_rag_pipeline.rag.policies', 'example_rag_pipeline.rag.question_answering', 'example_rag_pipeline.rag.retrieval', 'example_rag_pipeline.catalog']
['example_rag_pipeline.rag.annotation:annotate_documents', 'example_rag_pipeline.rag.evaluation:evaluate_answers', 'example_rag_pipeline.rag.indexer:create_vector_index', 'example_rag_pipeline.rag.policies:generate_questions', 'example_rag_pipeline.rag.question_answering:question_answering', 'example_rag_pipeline.rag.retrieval:filter_relevant', 'example_rag_pipeline.rag.retrieval:retrieve']
{('example_rag_pipeline.catalog', 'index'): IO(idx=ID1), ('example_rag_pipeline.catalog', 'llm_answers'): IO(idx=ID2), ('example_rag_pipeline.catalog', 'llm_model'): IO(idx=ID3), ('example_rag_pipeline.catalog', 'llm_vision_retrieval_model'): IO(idx=ID4), ('example_rag_pipeline.catalog', 'metrics'): IO(idx=ID5), ('example_rag_pipeline.catalog', 'pdf_documents'): IO(idx=ID6), ('example_rag_pipeline.catalog', 'pdfs_documents_annotated'): IO(idx=ID7), ('example_rag_pipeline.catalog', 'policies'): IO(idx=ID8), ('example_rag_pipeline.catalog', 'questions'): IO(idx=ID9), ('example_rag_pipeline.catalog', 'relevant_pages'): IO(idx=ID10), ('example_rag_pipeline.catalog', 'retrieved_pages'): IO(idx=ID11)}
['example_rag_pipeline.rag.annotation:annotate_documents', 'example_rag_pipeline.rag.evaluation:evaluate_answers', 'example_rag_pipeline.rag.indexer:create_vector_index', 'example_rag_pipeline.rag.policies:generate_questions', 'example_rag_pipeline.rag.question_answering:question_answering', 'example_rag_pipeline.rag.retrieval:filter_relevant', 'example_rag_pipeline.rag.retrieval:retrieve']

```