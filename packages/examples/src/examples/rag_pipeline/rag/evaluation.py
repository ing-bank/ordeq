from examples.rag_pipeline import catalog
from ordeq import node


@node(
    inputs=[catalog.llm_answers, catalog.llm_model], outputs=[catalog.metrics]
)
def evaluate_answers(answers, genai_model):
    """Evaluate answers"""
