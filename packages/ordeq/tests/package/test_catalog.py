from types import ModuleType

import pytest
from ordeq._catalog import CatalogError, check_catalogs_are_consistent
from ordeq._io import AnyIO
from ordeq_common import Literal, StringBuffer


class FakeModule(ModuleType):
    def __init__(self, name: str, d: dict[str, AnyIO]):
        super().__init__(name)
        self.name = name
        self.__dict__.update(d)

    @property
    def __name__(self) -> str:  # noqa: PLW3201
        return self.name


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (
            {
                # empty
            },
            {
                # empty
            },
        ),
        (
            {
                # empty
            },
            {
                "something_else": 4  # not an IO
            },
        ),
        ({"hello": StringBuffer()}, {"hello": Literal("hello")}),
        (
            {"hello": StringBuffer(), "result": StringBuffer()},
            {
                "hello": Literal("hello"),
                "result": StringBuffer(),
                "something_else": 4,  # not an IO
            },
        ),
    ],
)
def test_it_checks_consistent(a, b):
    catalog_a = FakeModule("catalog_a", a)
    catalog_b = FakeModule("catalog_b", b)
    check_catalogs_are_consistent(catalog_a, catalog_b)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (
            {"hello": StringBuffer(), "result": StringBuffer()},
            {
                "hello": Literal("hello")
                # result is mising
            },
        ),
        (
            {
                "hello": StringBuffer()
                # result is missing
            },
            {"hello": Literal("hello"), "result": StringBuffer()},
        ),
        (
            {
                # empty
            },
            {"hello": Literal("hello")},
        ),
        (
            {
                # empty but contains non-IO
                "something_else": 4
            },
            {"hello": Literal("hello"), "result": StringBuffer()},
        ),
    ],
)
def test_it_checks_inconsistent(a, b):
    catalog_a = FakeModule("catalog_a", a)
    catalog_b = FakeModule("catalog_b", b)
    with pytest.raises(CatalogError, match="Catalogs are inconsistent"):
        check_catalogs_are_consistent(catalog_a, catalog_b)
