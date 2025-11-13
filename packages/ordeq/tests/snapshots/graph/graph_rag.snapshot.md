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

node_graph = NodeGraph.from_graph(base_graph)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
Node:example_rag_pipeline.rag.annotation:annotate_documents --> io-2
Node:example_rag_pipeline.rag.evaluation:evaluate_answers --> io-5
Node:example_rag_pipeline.rag.indexer:create_vector_index --> io-15
Node:example_rag_pipeline.rag.policies:generate_questions --> io-16
Node:example_rag_pipeline.rag.question_answering:question_answering --> io-14
Node:example_rag_pipeline.rag.retrieval:retrieve --> io-19
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> io-21
io-14 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
io-14 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-6 --> Node:example_rag_pipeline.rag.annotation:annotate_documents
io-6 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-20 --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
io-20 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-20 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
io-17 --> Node:example_rag_pipeline.rag.indexer:create_vector_index
io-17 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-9 --> Node:example_rag_pipeline.rag.policies:generate_questions
io-16 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-16 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-21 --> Node:example_rag_pipeline.rag.question_answering:question_answering
io-15 --> Node:example_rag_pipeline.rag.retrieval:retrieve
io-19 --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
NodeGraph
Node:example_rag_pipeline.rag.annotation:annotate_documents
Node:example_rag_pipeline.rag.evaluation:evaluate_answers
Node:example_rag_pipeline.rag.indexer:create_vector_index --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.question_answering:question_answering
Node:example_rag_pipeline.rag.policies:generate_questions --> Node:example_rag_pipeline.rag.retrieval:retrieve
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.annotation:annotate_documents
Node:example_rag_pipeline.rag.question_answering:question_answering --> Node:example_rag_pipeline.rag.evaluation:evaluate_answers
Node:example_rag_pipeline.rag.retrieval:retrieve --> Node:example_rag_pipeline.rag.retrieval:filter_relevant
Node:example_rag_pipeline.rag.retrieval:filter_relevant --> Node:example_rag_pipeline.rag.question_answering:question_answering
Topological ordering
['example_rag_pipeline.rag.policies:generate_questions',
 'example_rag_pipeline.rag.indexer:create_vector_index',
 'example_rag_pipeline.rag.retrieval:retrieve',
 'example_rag_pipeline.rag.retrieval:filter_relevant',
 'example_rag_pipeline.rag.question_answering:question_answering',
 'example_rag_pipeline.rag.evaluation:evaluate_answers',
 'example_rag_pipeline.rag.annotation:annotate_documents']

```