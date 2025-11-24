from dataclasses import dataclass

import pytest
from ordeq import Input, IOException
from ordeq_common import Dataclass


@dataclass
class Fruit:
    name: str
    colour: str


def test_it_loads():
    assert Dataclass(
        Input({"name": "banana", "colour": "yellow"}), Fruit
    ).load() == Fruit(name="banana", colour="yellow")


def test_it_errors_for_invalid_data():
    with pytest.raises(IOException, match="unexpected keyword"):
        Dataclass(Input({"name": "banana", "weight_gr": "100g"}), Fruit).load()
