from ordeq import node

from rag_pipeline import catalog


@node(
    inputs=[catalog.llm_answers, catalog.llm_model], outputs=[catalog.metrics]
)
def evaluate_answers(answers, genai_model):
    """Evaluate answers"""
    # Implementation would go here
