## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_runnables_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_rag_pipeline.rag"),
    importlib.import_module("example_rag_pipeline.catalog"),
]

modules = [mod.__name__ for mod in _resolve_runnables_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Output

```text
['example_rag_pipeline.catalog',
 'example_rag_pipeline.rag',
 'example_rag_pipeline.rag.annotation',
 'example_rag_pipeline.rag.evaluation',
 'example_rag_pipeline.rag.indexer',
 'example_rag_pipeline.rag.policies',
 'example_rag_pipeline.rag.question_answering',
 'example_rag_pipeline.rag.retrieval']
['example_rag_pipeline.rag.annotation:annotate_documents',
 'example_rag_pipeline.rag.evaluation:evaluate_answers',
 'example_rag_pipeline.rag.indexer:create_vector_index',
 'example_rag_pipeline.rag.policies:generate_questions',
 'example_rag_pipeline.rag.question_answering:question_answering',
 'example_rag_pipeline.rag.retrieval:filter_relevant',
 'example_rag_pipeline.rag.retrieval:retrieve']
{'example_rag_pipeline.catalog': {'index': IO(idx=ID1),
                                  'llm_answers': IO(idx=ID2),
                                  'llm_model': IO(idx=ID3),
                                  'llm_vision_retrieval_model': IO(idx=ID4),
                                  'metrics': IO(idx=ID5),
                                  'pdf_documents': IO(idx=ID6),
                                  'pdfs_documents_annotated': IO(idx=ID7),
                                  'policies': IO(idx=ID8),
                                  'questions': IO(idx=ID9),
                                  'relevant_pages': IO(idx=ID10),
                                  'retrieved_pages': IO(idx=ID11)}}
['example_rag_pipeline.rag.annotation:annotate_documents',
 'example_rag_pipeline.rag.evaluation:evaluate_answers',
 'example_rag_pipeline.rag.indexer:create_vector_index',
 'example_rag_pipeline.rag.policies:generate_questions',
 'example_rag_pipeline.rag.question_answering:question_answering',
 'example_rag_pipeline.rag.retrieval:filter_relevant',
 'example_rag_pipeline.rag.retrieval:retrieve']

```