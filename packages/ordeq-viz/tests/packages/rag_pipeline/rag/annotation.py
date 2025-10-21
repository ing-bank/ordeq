from ordeq import node

from rag_pipeline import catalog


@node(
    inputs=[catalog.llm_answers, catalog.pdf_documents],
    outputs=[catalog.pdfs_documents_annotated],
)
def annotate_documents(x, y):
    """Annotate documents with answers from the LLM"""
