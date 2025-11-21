## Resource

```python
from pprint import pprint

import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_rag_pipeline))
print("Nodes:")
pprint(list(nodes.values()), width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
[('example_rag_pipeline.rag.annotation', 'annotate_documents'),
 ('example_rag_pipeline.rag.evaluation', 'evaluate_answers'),
 ('example_rag_pipeline.rag.indexer', 'create_vector_index'),
 ('example_rag_pipeline.rag.policies', 'generate_questions'),
 ('example_rag_pipeline.rag.question_answering', 'question_answering'),
 ('example_rag_pipeline.rag.retrieval', 'retrieve'),
 ('example_rag_pipeline.rag.retrieval', 'filter_relevant')]
IOs:
[('example_rag_pipeline.catalog', 'policies'),
 ('example_rag_pipeline.catalog', 'llm_model'),
 ('example_rag_pipeline.catalog', 'llm_vision_retrieval_model'),
 ('example_rag_pipeline.catalog', 'pdf_documents'),
 ('example_rag_pipeline.catalog', 'retrieved_pages'),
 ('example_rag_pipeline.catalog', 'relevant_pages'),
 ('example_rag_pipeline.catalog', 'index'),
 ('example_rag_pipeline.catalog', 'questions'),
 ('example_rag_pipeline.catalog', 'metrics'),
 ('example_rag_pipeline.catalog', 'pdfs_documents_annotated'),
 ('example_rag_pipeline.catalog', 'llm_answers')]

```