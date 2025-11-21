## Resource

```python
from pprint import pprint

import example_rag_pipeline
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_rag_pipeline))
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
Nodes:
{<function annotate_documents at HASH1>: (('example_rag_pipeline.rag.annotation',
                                                 'annotate_documents'),
                                                <function annotate_documents at HASH1>),
 <function evaluate_answers at HASH2>: (('example_rag_pipeline.rag.evaluation',
                                               'evaluate_answers'),
                                              <function evaluate_answers at HASH2>),
 <function create_vector_index at HASH3>: (('example_rag_pipeline.rag.indexer',
                                                  'create_vector_index'),
                                                 <function create_vector_index at HASH3>),
 <function generate_questions at HASH4>: (('example_rag_pipeline.rag.policies',
                                                 'generate_questions'),
                                                <function generate_questions at HASH4>),
 <function question_answering at HASH5>: (('example_rag_pipeline.rag.question_answering',
                                                 'question_answering'),
                                                <function question_answering at HASH5>),
 <function retrieve at HASH6>: (('example_rag_pipeline.rag.retrieval',
                                       'retrieve'),
                                      <function retrieve at HASH6>),
 <function filter_relevant at HASH7>: (('example_rag_pipeline.rag.retrieval',
                                              'filter_relevant'),
                                             <function filter_relevant at HASH7>)}
IOs:
[(('example_rag_pipeline.catalog',
   'policies'),
  IO(id=ID1)),
 (('example_rag_pipeline.catalog',
   'llm_model'),
  IO(id=ID2)),
 (('example_rag_pipeline.catalog',
   'llm_vision_retrieval_model'),
  IO(id=ID3)),
 (('example_rag_pipeline.catalog',
   'pdf_documents'),
  IO(id=ID4)),
 (('example_rag_pipeline.catalog',
   'retrieved_pages'),
  IO(id=ID5)),
 (('example_rag_pipeline.catalog',
   'relevant_pages'),
  IO(id=ID6)),
 (('example_rag_pipeline.catalog',
   'index'),
  IO(id=ID7)),
 (('example_rag_pipeline.catalog',
   'questions'),
  IO(id=ID8)),
 (('example_rag_pipeline.catalog',
   'metrics'),
  IO(id=ID9)),
 (('example_rag_pipeline.catalog',
   'pdfs_documents_annotated'),
  IO(id=ID10)),
 (('example_rag_pipeline.catalog',
   'llm_answers'),
  IO(id=ID11))]

```