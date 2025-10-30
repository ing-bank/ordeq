from ordeq import node

from examples.rag_pipeline import catalog


@node(inputs=[catalog.policies], outputs=[catalog.questions])
def generate_questions(policies):
    """Generate questions from policies"""
