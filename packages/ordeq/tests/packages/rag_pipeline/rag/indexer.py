from ordeq import node
from rag_pipeline import catalog


@node(
    inputs=[catalog.pdf_documents, catalog.llm_vision_retrieval_model],
    outputs=[catalog.index],
)
def create_vector_index(documents, genai_model):
    """Create a vector index"""
