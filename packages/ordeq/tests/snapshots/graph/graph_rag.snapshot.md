## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_rag_pipeline
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_rag_pipeline)
node_io_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph:")
print(node_io_graph)

node_graph = NodeGraph.from_graph(node_io_graph)
print("NodeGraph:")
print(node_graph)

print("Topological ordering:")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph:
<ordeq._graph.NodeIOGraph object at HASH1>
NodeGraph:
NodeGraph(edges=defaultdict(<class 'ordeq._graph.OrderedSet'>, {Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)]): {Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID3), IO(idx=ID4), IO(idx=ID2)], outputs=[IO(idx=ID5)]): None}, Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID4)]): {Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID4), IO(idx=ID7), IO(idx=ID8)], outputs=[IO(idx=ID9)]): None, Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID3), IO(idx=ID4), IO(idx=ID2)], outputs=[IO(idx=ID5)]): None}, Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID4), IO(idx=ID7), IO(idx=ID8)], outputs=[IO(idx=ID9)]): {Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID9), IO(idx=ID1)], outputs=[IO(idx=ID10)]): None, Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID9), IO(idx=ID8)], outputs=[IO(idx=ID11)]): None}, Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID5), IO(idx=ID8)], outputs=[IO(idx=ID7)]): {Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID4), IO(idx=ID7), IO(idx=ID8)], outputs=[IO(idx=ID9)]): None}, Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID3), IO(idx=ID4), IO(idx=ID2)], outputs=[IO(idx=ID5)]): {Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID5), IO(idx=ID8)], outputs=[IO(idx=ID7)]): None}}), nodes={Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID9), IO(idx=ID1)], outputs=[IO(idx=ID10)]): None, Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID9), IO(idx=ID8)], outputs=[IO(idx=ID11)]): None, Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)]): None, Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID4)]): None, Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID4), IO(idx=ID7), IO(idx=ID8)], outputs=[IO(idx=ID9)]): None, Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID5), IO(idx=ID8)], outputs=[IO(idx=ID7)]): None, Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID3), IO(idx=ID4), IO(idx=ID2)], outputs=[IO(idx=ID5)]): None})
Topological ordering:
(Node(name=example_rag_pipeline.rag.policies:generate_questions, inputs=[IO(idx=ID6)], outputs=[IO(idx=ID4)]),
 Node(name=example_rag_pipeline.rag.indexer:create_vector_index, inputs=[IO(idx=ID1), IO(idx=ID2)], outputs=[IO(idx=ID3)]),
 Node(name=example_rag_pipeline.rag.retrieval:retrieve, inputs=[IO(idx=ID3), IO(idx=ID4), IO(idx=ID2)], outputs=[IO(idx=ID5)]),
 Node(name=example_rag_pipeline.rag.retrieval:filter_relevant, inputs=[IO(idx=ID5), IO(idx=ID8)], outputs=[IO(idx=ID7)]),
 Node(name=example_rag_pipeline.rag.question_answering:question_answering, inputs=[IO(idx=ID4), IO(idx=ID7), IO(idx=ID8)], outputs=[IO(idx=ID9)]),
 Node(name=example_rag_pipeline.rag.evaluation:evaluate_answers, inputs=[IO(idx=ID9), IO(idx=ID8)], outputs=[IO(idx=ID11)]),
 Node(name=example_rag_pipeline.rag.annotation:annotate_documents, inputs=[IO(idx=ID9), IO(idx=ID1)], outputs=[IO(idx=ID10)]))

```