import importlib

import pytest
from ordeq.framework._gather import _collect_nodes_and_ios


@pytest.mark.parametrize(
    ("imports", "expected_nodes", "expected_ios"),
    [
        pytest.param(["example"], [], [], id="example"),
        pytest.param(
            [
                "example",
                "example",
                "example",
                "example.wrapped_io",
                "example.nodes",
            ],
            [
                "example.nodes:world",
                "example.wrapped_io:hello",
                "example.wrapped_io:print_message",
            ],
            [
                "message:SayHello",
                "name_generator:NameGenerator",
                "name_printer:NamePrinter",
                "x:StringBuffer",
                "y:StringBuffer",
            ],
            id="example_repeated_runnables",
        ),
        pytest.param(
            ["example.wrapped_io"],
            ["example.wrapped_io:hello", "example.wrapped_io:print_message"],
            [
                "message:SayHello",
                "name_generator:NameGenerator",
                "name_printer:NamePrinter",
            ],
            id="example_wrapped_io",
        ),
        pytest.param(["example2"], [], [], id="example2"),
        pytest.param(["example3"], [], [], id="example3"),
        pytest.param(["duplicates"], [], [], id="duplicates"),
        pytest.param(["nested"], [], [], id="nested"),
        pytest.param(["function_reuse"], [], [], id="function_reuse"),
        pytest.param(
            ["function_reuse.nodes"],
            [
                "function_reuse.func_defs:print_input",
                "function_reuse.func_defs:print_input",
                "function_reuse.func_defs:print_input",
                "function_reuse.func_defs:print_input",
                "function_reuse.nodes:pi",
            ],
            ["A:StringBuffer", "B:StringBuffer"],
            id="function_reuse_nodes_only",
        ),
        pytest.param(["rag_pipeline"], [], [], id="rag_pipeline"),
        pytest.param(
            ["rag_pipeline", "rag_pipeline.rag"], [], [], id="rag_pipeline+rag"
        ),
        pytest.param(
            ["rag_pipeline.rag", "rag_pipeline.catalog"],
            [],
            [
                "index:IO",
                "llm_answers:IO",
                "llm_model:IO",
                "llm_vision_retrieval_model:IO",
                "metrics:IO",
                "pdf_documents:IO",
                "pdfs_documents_annotated:IO",
                "policies:IO",
                "questions:IO",
                "relevant_pages:IO",
                "retrieved_pages:IO",
            ],
            id="rag_rag+catalog",
        ),
        pytest.param(["rag_pipeline.rag"], [], [], id="rag_rag"),
        pytest.param(
            [
                "rag_pipeline.rag.annotation",
                "rag_pipeline.rag.evaluation",
                "rag_pipeline.rag.indexer",
                "rag_pipeline.rag.policies",
                "rag_pipeline.rag.question_answering",
                "rag_pipeline.rag.retrieval",
            ],
            [
                "rag_pipeline.rag.annotation:annotate_documents",
                "rag_pipeline.rag.evaluation:evaluate_answers",
                "rag_pipeline.rag.indexer:create_vector_index",
                "rag_pipeline.rag.policies:generate_questions",
                "rag_pipeline.rag.question_answering:question_answering",
                "rag_pipeline.rag.retrieval:filter_relevant",
                "rag_pipeline.rag.retrieval:retrieve",
            ],
            [],
            id="rag_pipeline_all",
        ),
        pytest.param(
            [
                "rag_pipeline.rag.annotation",
                "rag_pipeline.rag.evaluation",
                "rag_pipeline.rag.indexer",
                "rag_pipeline.rag.policies",
                "rag_pipeline.rag.question_answering",
                "rag_pipeline.rag.retrieval",
                "rag_pipeline.catalog",
            ],
            [
                "rag_pipeline.rag.annotation:annotate_documents",
                "rag_pipeline.rag.evaluation:evaluate_answers",
                "rag_pipeline.rag.indexer:create_vector_index",
                "rag_pipeline.rag.policies:generate_questions",
                "rag_pipeline.rag.question_answering:question_answering",
                "rag_pipeline.rag.retrieval:filter_relevant",
                "rag_pipeline.rag.retrieval:retrieve",
            ],
            [
                "index:IO",
                "llm_answers:IO",
                "llm_model:IO",
                "llm_vision_retrieval_model:IO",
                "metrics:IO",
                "pdf_documents:IO",
                "pdfs_documents_annotated:IO",
                "policies:IO",
                "questions:IO",
                "relevant_pages:IO",
                "retrieved_pages:IO",
            ],
            id="rag_pipeline_all+catalog",
        ),
    ],
)
def test_gather_nodes_and_ios_from_package(
    imports: list[str],
    expected_nodes,
    expected_ios,
    append_packages_dir_to_sys_path,
) -> None:
    """Test gathering nodes and IOs from a package."""

    runnables = [
        importlib.import_module(import_path) for import_path in imports
    ]

    nodes, ios = _collect_nodes_and_ios(*runnables)
    assert expected_nodes == sorted(n.name for n in nodes)
    assert expected_ios == sorted([
        f"{name}:{type(io).__name__}" for name, io in ios.items()
    ])
