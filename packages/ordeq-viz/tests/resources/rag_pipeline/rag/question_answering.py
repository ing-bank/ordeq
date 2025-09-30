from rag_pipeline import catalog

from ordeq import node
@node(inputs=[catalog.questions, catalog.relevant_pages, catalog.llm_model], outputs=[catalog.llm_answers])
def question_answering(questions, pages, model):
    """Generate question answers"""
    pass
