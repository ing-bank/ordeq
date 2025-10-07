from dataclasses import dataclass

import pytest
from ordeq.framework.io import IOException
from ordeq_common import Dataclass, Literal


@dataclass
class Fruit:
    name: str
    colour: str


def test_it_loads():
    assert Dataclass(
        Literal({"name": "banana", "colour": "yellow"}), Fruit
    ).load() == Fruit(name="banana", colour="yellow")


def test_it_errors_for_invalid_data():
    with pytest.raises(IOException, match="unexpected keyword"):
        Dataclass(
            Literal({"name": "banana", "weight_gr": "100g"}), Fruit
        ).load()
