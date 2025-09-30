from rag_pipeline import catalog

from ordeq import node


@node(inputs=[catalog.policies], outputs=[catalog.questions])
def generate_questions(policies):
    """Generate questions from policies"""
    # Implementation would go here
    pass
