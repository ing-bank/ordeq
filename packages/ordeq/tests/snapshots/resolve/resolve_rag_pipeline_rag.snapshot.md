## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [
    importlib.import_module("example_rag_pipeline"),
    importlib.import_module("example_rag_pipeline.rag"),
]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_rag_pipeline',
 'example_rag_pipeline.catalog',
 'example_rag_pipeline.rag',
 'example_rag_pipeline.rag.annotation',
 'example_rag_pipeline.rag.evaluation',
 'example_rag_pipeline.rag.indexer',
 'example_rag_pipeline.rag.policies',
 'example_rag_pipeline.rag.question_answering',
 'example_rag_pipeline.rag.retrieval']
[(FQN(module='example_rag_pipeline.rag.annotation', name='annotate_documents'),
  Node(module=example_rag_pipeline.rag.annotation, name=annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)])),
 (FQN(module='example_rag_pipeline.rag.evaluation', name='evaluate_answers'),
  Node(module=example_rag_pipeline.rag.evaluation, name=evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)])),
 (FQN(module='example_rag_pipeline.rag.indexer', name='create_vector_index'),
  Node(module=example_rag_pipeline.rag.indexer, name=create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)])),
 (FQN(module='example_rag_pipeline.rag.policies', name='generate_questions'),
  Node(module=example_rag_pipeline.rag.policies, name=generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)])),
 (FQN(module='example_rag_pipeline.rag.question_answering', name='question_answering'),
  Node(module=example_rag_pipeline.rag.question_answering, name=question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='retrieve'),
  Node(module=example_rag_pipeline.rag.retrieval, name=retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='filter_relevant'),
  Node(module=example_rag_pipeline.rag.retrieval, name=filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]))]
{'example_rag_pipeline.catalog': {'index': IO(id=ID7),
                                  'llm_answers': IO(id=ID1),
                                  'llm_model': IO(id=ID4),
                                  'llm_vision_retrieval_model': IO(id=ID6),
                                  'metrics': IO(id=ID5),
                                  'pdf_documents': IO(id=ID2),
                                  'pdfs_documents_annotated': IO(id=ID3),
                                  'policies': IO(id=ID8),
                                  'questions': IO(id=ID9),
                                  'relevant_pages': IO(id=ID10),
                                  'retrieved_pages': IO(id=ID11)}}
[(FQN(module='example_rag_pipeline.rag.annotation', name='annotate_documents'),
  Node(module=example_rag_pipeline.rag.annotation, name=annotate_documents, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)])),
 (FQN(module='example_rag_pipeline.rag.evaluation', name='evaluate_answers'),
  Node(module=example_rag_pipeline.rag.evaluation, name=evaluate_answers, inputs=[IO(id=ID1), IO(id=ID4)], outputs=[IO(id=ID5)])),
 (FQN(module='example_rag_pipeline.rag.indexer', name='create_vector_index'),
  Node(module=example_rag_pipeline.rag.indexer, name=create_vector_index, inputs=[IO(id=ID2), IO(id=ID6)], outputs=[IO(id=ID7)])),
 (FQN(module='example_rag_pipeline.rag.policies', name='generate_questions'),
  Node(module=example_rag_pipeline.rag.policies, name=generate_questions, inputs=[IO(id=ID8)], outputs=[IO(id=ID9)])),
 (FQN(module='example_rag_pipeline.rag.question_answering', name='question_answering'),
  Node(module=example_rag_pipeline.rag.question_answering, name=question_answering, inputs=[IO(id=ID9), IO(id=ID10), IO(id=ID4)], outputs=[IO(id=ID1)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='retrieve'),
  Node(module=example_rag_pipeline.rag.retrieval, name=retrieve, inputs=[IO(id=ID7), IO(id=ID9), IO(id=ID6)], outputs=[IO(id=ID11)])),
 (FQN(module='example_rag_pipeline.rag.retrieval', name='filter_relevant'),
  Node(module=example_rag_pipeline.rag.retrieval, name=filter_relevant, inputs=[IO(id=ID11), IO(id=ID4)], outputs=[IO(id=ID10)]))]

```

## Warnings

```text
UserWarning: Module 'example_rag_pipeline.rag' already provided as runnable
```