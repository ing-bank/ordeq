from rag_pipeline import catalog

from ordeq import node


@node(inputs=[catalog.index, catalog.questions, catalog.llm_vision_retrieval_model], outputs=[catalog.retrieved_pages])
def retrieve(index, questions, llm_model):
    """Retrieve relevant documents"""


@node(inputs=[catalog.retrieved_pages, catalog.llm_model], outputs=[catalog.relevant_pages])
def filter_relevant(retrieved_pages, llm_model):
    """Filter the retrieved documents"""

