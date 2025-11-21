from unittest.mock import Mock

from ordeq import Node
from ordeq._fqn import Unknown
from ordeq._process_nodes import _collect_views


def test_collect_views():
    # Edge case: empty set
    assert _collect_views() == ()

    # Node with no views
    node1 = Mock()
    node1.views = []
    fq_node1 = (("module", "node1"), node1)
    assert _collect_views(fq_node1) == (fq_node1,)

    # Node with a single view
    view1 = Mock(spec=Node)
    view1.views = []
    node2 = Mock(spec=Node)
    node2.views = [view1]
    fq_node2 = (("module", "node2"), node2)
    assert _collect_views(fq_node2) == (fq_node2, ((Unknown, Unknown), view1))

    # Node with multiple views
    view2 = Mock(spec=Node)
    view2.views = []
    view3 = Mock(spec=Node)
    view3.views = []
    node3 = Mock()
    node3.views = [view2, view3]
    fq_node3 = (("module", "node3"), node3)
    assert _collect_views(fq_node3) == (
        fq_node3,
        ((Unknown, Unknown), view2),
        ((Unknown, Unknown), view3),
    )

    # Nested views: a view that itself has a view
    nested_view = Mock(spec=Node)
    nested_view.views = []
    view4 = Mock(spec=Node)
    view4.views = [nested_view]
    node4 = Mock(spec=Node)
    node4.views = [view4]
    fq_node4 = (("module", "node4"), node4)
    # collect_views should recursively collect nested_view
    assert _collect_views(fq_node4) == (
        fq_node4,
        ((Unknown, Unknown), view4),
        ((Unknown, Unknown), nested_view),
    )

    # Multiple nodes with overlapping views
    node5 = Mock(spec=Node)
    node6 = Mock(spec=Node)
    view1.views = []
    view2.views = []
    view3.views = []
    node5.views = [view1, view2]
    node6.views = [view2, view3]
    fq_node5 = (("module", "node5"), node5)
    fq_node6 = (("module", "node6"), node6)
    assert _collect_views(fq_node5, fq_node6) == (
        fq_node5,
        ((Unknown, Unknown), view1),
        ((Unknown, Unknown), view2),
        fq_node6,
        ((Unknown, Unknown), view3),
    )

    # Same example as above but different order of args
    # This shows that the collection is ordered
    node5 = Mock(spec=Node)
    node6 = Mock(spec=Node)
    view1.views = []
    view2.views = []
    view3.views = []
    node5.views = [view1, view2]
    node6.views = [view2, view3]
    assert _collect_views(fq_node6, fq_node5) == (
        fq_node6,
        ((Unknown, Unknown), view2),
        ((Unknown, Unknown), view3),
        fq_node5,
        ((Unknown, Unknown), view1),
    )
