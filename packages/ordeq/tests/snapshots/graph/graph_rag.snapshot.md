## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
io-0 --> Node:example_rag_pipeline.rag.policies:generate_questions
io-1 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-1 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-2 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-2 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
Node:example_rag_pipeline.rag.policies:generate_questions --> io-3
Node:example_rag_pipeline.rag.indexer:create_vector_index --> io-4
io-3 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-3 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-4 --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.retrieval:retrieve --> io-6
io-5 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
io-5 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-5 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-6 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> io-7
io-7 --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.question_answering:question_answering --> io-8
io-8 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-8 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
Node:example_rag_pipeline.rag.annotation:annotate_documents --> io-9
Node:example_rag_pipeline.rag.evaluation:evaluate_answers --> io-10
NodeGraph
Node:example_rag_pipeline.rag.indexer:create_vector_index --> Node:example_rag_pipeline.rag.indexer:create_vector_index
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.policies:generate_questions
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.policies:generate_questions
Node:example_rag_pipeline.rag.retrieval:retrieve --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.evaluation:evaluate_answers
Node:example_rag_pipeline.rag.annotation:annotate_documents
Topological ordering
(Node(module=example_rag_pipeline.rag.indexer, name=create_vector_index, inputs=[IO(id=ID1), IO(id=ID2)], outputs=[IO(id=ID3)]),
 Node(module=example_rag_pipeline.rag.policies, name=generate_questions, inputs=[IO(id=ID4)], outputs=[IO(id=ID5)]),
 Node(module=example_rag_pipeline.rag.retrieval, name=retrieve, inputs=[IO(id=ID3), IO(id=ID5), IO(id=ID2)], outputs=[IO(id=ID6)]),
 Node(module=example_rag_pipeline.rag.retrieval, name=filter_relevant, inputs=[IO(id=ID6), IO(id=ID7)], outputs=[IO(id=ID8)]),
 Node(module=example_rag_pipeline.rag.question_answering, name=question_answering, inputs=[IO(id=ID5), IO(id=ID8), IO(id=ID7)], outputs=[IO(id=ID9)]),
 Node(module=example_rag_pipeline.rag.evaluation, name=evaluate_answers, inputs=[IO(id=ID9), IO(id=ID7)], outputs=[IO(id=ID10)]),
 Node(module=example_rag_pipeline.rag.annotation, name=annotate_documents, inputs=[IO(id=ID9), IO(id=ID1)], outputs=[IO(id=ID11)]))

```