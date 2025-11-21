## Resource

```python
from pprint import pprint

import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_rag_pipeline))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
Nodes:
{<function filter_relevant at HASH1>: ('example_rag_pipeline.rag.retrieval', 'filter_relevant'),
 <function retrieve at HASH2>: ('example_rag_pipeline.rag.retrieval', 'retrieve'),
 <function question_answering at HASH3>: ('example_rag_pipeline.rag.question_answering', 'question_answering'),
 <function generate_questions at HASH4>: ('example_rag_pipeline.rag.policies', 'generate_questions'),
 <function annotate_documents at HASH5>: ('example_rag_pipeline.rag.annotation', 'annotate_documents'),
 <function create_vector_index at HASH6>: ('example_rag_pipeline.rag.indexer', 'create_vector_index'),
 <function evaluate_answers at HASH7>: ('example_rag_pipeline.rag.evaluation', 'evaluate_answers')}
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