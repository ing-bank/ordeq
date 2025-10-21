from ordeq_common import Literal
from ordeq_pydantic import PydanticModel
from ordeq_toml import TOML
from ordeq_yaml import YAML
from pydantic import BaseModel


class MyModel(BaseModel):
    hello: str
    world: str


def test_model(tmp_path):
    example = Literal({"hello": "hello", "world": "world"})
    dataset = PydanticModel(io=example, model_type=MyModel)

    loaded_model = dataset.load()
    assert loaded_model.hello == "hello"
    assert loaded_model.world == "world"


def test_model_toml(tmp_path):
    toml_content = """
hello = 'hello'
world = 'world'
"""
    toml_path = tmp_path / "example.toml"
    toml_path.write_text(toml_content)
    example = TOML(path=toml_path)
    dataset = PydanticModel(io=example, model_type=MyModel)
    loaded_model = dataset.load()
    assert loaded_model.hello == "hello"
    assert loaded_model.world == "world"


def test_model_yaml(tmp_path):
    yaml_content = """
hello: hello
world: world
"""
    yaml_path = tmp_path / "example.yaml"
    yaml_path.write_text(yaml_content)
    example = YAML(path=yaml_path)
    dataset = PydanticModel(io=example, model_type=MyModel)
    loaded_model = dataset.load()
    assert loaded_model.hello == "hello"
    assert loaded_model.world == "world"
