from rag_pipeline import catalog

from ordeq import node


@node(inputs=[catalog.pdf_documents, catalog.llm_vision_retrieval_model], outputs=[catalog.index])
def create_vector_index(documents, genai_model):
    """Create a vector index"""
    # Implementation would go here
    pass
