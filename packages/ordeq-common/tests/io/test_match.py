from ordeq_args import EnvironmentVariable
from ordeq_common import Literal, Match


def test_wraps_match_on_load():
    ev = EnvironmentVariable("COUNTRY")
    s1 = Literal("Netherlands")
    s2 = Literal("Belgium")
    country = Match(ev).Case("NL", s1).Case("BE", s2)
    assert country.references == {"io": [ev], "cases": [s1, s2]}


def test_wraps_match_on_save():
    small = EnvironmentVariable("SMALL")
    large = EnvironmentVariable("LARGE")
    small_or_large = Match().Case("S", small).Case("L", large)
    small_or_large.save(("S", "Andorra"))
    small_or_large.save(("L", "Russia"))

    assert small_or_large.references == {"cases": [small, large]}
