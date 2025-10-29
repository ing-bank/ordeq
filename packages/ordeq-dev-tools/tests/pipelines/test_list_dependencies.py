"""Tests for the list_dependencies pipeline."""

from ordeq_dev_tools.pipelines.list_dependencies import (
    compute_affected_dependencies,
)


def test_compute_affected_dependencies():
    """Test the compute_affected_dependencies function."""
    deps_by_package = {
        "ordeq-a": [],
        "ordeq-b": ["ordeq-a"],
        "ordeq-c": ["ordeq-b"],
        "ordeq-d": ["ordeq-a", "ordeq-c"],
        "ordeq-e": [],
    }

    expected_affected = {
        "ordeq-a": ["ordeq-b", "ordeq-c", "ordeq-d"],
        "ordeq-b": ["ordeq-c", "ordeq-d"],
        "ordeq-c": ["ordeq-d"],
        "ordeq-d": [],
        "ordeq-e": [],
    }

    affected = compute_affected_dependencies(deps_by_package)

    assert affected == expected_affected
